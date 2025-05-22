# main.py
import uuid, os, asyncio
from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sse_starlette.sse import EventSourceResponse
from yt_dlp import YoutubeDL
from speechbrain.inference.classifiers import EncoderClassifier
import json
app = FastAPI()
# 1. Mount CSS/JS under /static
app.mount("/static", StaticFiles(directory="static"), name="static")

progress = {}

# 2. Load ECAPA-TDNN model once
ecapa = EncoderClassifier.from_hparams(
    source="Jzuluaga/accent-id-commonaccent_ecapa",
    savedir="ecapa_model",
    run_opts={"device":"auto"}
)

def download_and_classify(url: str, task_id: str):
    progress[task_id] = {"status": "downloading", "progress": 10}
    ydl_opts = {"format": "bestaudio/best", "outtmpl": f"{task_id}.%(ext)s"}
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
    progress[task_id] = {"status": "extracting audio", "progress": 50}
    filepath = ydl.prepare_filename(info)
    progress[task_id] = {"status": "detecting accent", "progress": 80}
    out_prob, score, index, label = ecapa.classify_file(filepath)
    conf = float(score.item()) * 100
    progress[task_id] = {
        "status": "finished",
        "label": label[0],
        "confidence": f"{conf:.1f}%"
    }
    os.remove(filepath)
from pydantic import BaseModel

class VideoURL(BaseModel):
    url: str

@app.post("/process")
async def process_video(data: VideoURL, background_tasks: BackgroundTasks):
    task_id = str(uuid.uuid4())
    progress[task_id] = 0
    background_tasks.add_task(download_and_classify, data.url, task_id)
    return {"task_id": task_id}


@app.get("/progress/{task_id}")
async def progress_stream(task_id: str):
    async def event_generator():
        while True:
            data = progress.get(task_id)
            yield {"data": json.dumps(data)}
            if isinstance(data, dict) and data.get('status') == "finished":
                break
            await asyncio.sleep(0.5)
    return EventSourceResponse(event_generator())

# 3. Serve index.html for root and direct /index.html requests
@app.get("/", include_in_schema=False)
@app.get("/index.html", include_in_schema=False)
async def root():
    return FileResponse("static/index.html")

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

# English-Accent-Detector

[![FastAPI](https://img.shields.io/badge/Framework-FastAPI-009688?style=flat-square)](https://fastapi.tiangolo.com/)
[![SpeechBrain](https://img.shields.io/badge/Speech-Accent_ID-blueviolet?style=flat-square)](https://speechbrain.readthedocs.io/en/latest/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A modern, web-based application for automatic **English accent detection** using deep learning.  
Built with **FastAPI**, **SpeechBrain ECAPA**, and **yt-dlp** for robust and flexible audio extraction and classification.

---

## 🚀 Features

- **Detects speaker’s English accent** (e.g., British, American, Australian, etc.) from any public video URL
- **Confidence score** visualization with an animated circular chart
- Supports YouTube, Loom, direct MP4 links, and any public video/audio URL
- Real-time progress updates and status visualization
- Friendly, responsive web UI

---

## 🖥️ Live Demo / Test Link

> Try with this public MP4 speech video:  
> [https://voa-video-ns.akamaized.net/pangeavideo/2025/03/0/04/04dc51b7-6304-4483-06e7-08dd5c8b1668_240p.mp4?download=1](https://voa-video-ns.akamaized.net/pangeavideo/2025/03/0/04/04dc51b7-6304-4483-06e7-08dd5c8b1668_240p.mp4?download=1)

---

## ⚡ Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/DoubleM01/English-Accent-Detector.git
cd English-Accent-Detector
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```
- Python 3.8+ recommended

### 3. Run the Application

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### 4. Open in Browser

Visit: [http://localhost:8000/index.html](http://localhost:8000/index.html)

---

## 🛠️ Usage

1. **Paste any public video or direct mp4 URL** in the input box (e.g., the test link above).
2. Click “Analyze Accent”.
3. Watch real-time progress and final prediction:
    - **Accent** (e.g., American, British)
    - **Confidence Score** as a circular chart

> **Note:** Only public videos are supported. Restricted or login-required content will not work.

---

## 🧠 How It Works

- **yt-dlp** downloads and extracts audio from public video URLs.
- **SpeechBrain ECAPA** model analyzes the audio and predicts the accent.
- **FastAPI** serves the backend and SSE for real-time UI updates.
- **Frontend** shows animated progress/status and displays results with a modern design.

---

## 📦 Dependencies

- [FastAPI](https://fastapi.tiangolo.com/)
- [uvicorn](https://www.uvicorn.org/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [SpeechBrain](https://speechbrain.readthedocs.io/en/latest/)
- [PyTorch](https://pytorch.org/)
- [sse-starlette](https://pypi.org/project/sse-starlette/)

See `requirements.txt` for details.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Acknowledgments

- [SpeechBrain: ECAPA Accent ID](https://huggingface.co/Jzuluaga/accent-id-commonaccent_ecapa)

---

**For issues or contributions, please submit a pull request or open an issue on [GitHub](https://github.com/DoubleM01/English-Accent-Detector/).**

---




**Test Video:**  

https://github.com/user-attachments/assets/1be581b2-4e87-4797-9b00-3c623087bcb6


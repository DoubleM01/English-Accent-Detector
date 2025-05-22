function animateConfidenceCircle(percent) {
  const circle = document.getElementById('progressCircle');
  const text = document.getElementById('confidenceText');
  const radius = 54;
  const circumference = 2 * Math.PI * radius;
  // Animate
  circle.style.strokeDasharray = `${circumference}`;
  let offset = circumference * (1 - percent / 100);
  circle.style.strokeDashoffset = offset;

  // Animate number count up
  let current = 0;
  text.textContent = '0%';
  document.getElementById('circle-container').style.display = 'flex';
  const step = Math.ceil(percent / 30);
  let interval = setInterval(() => {
    current += step;
    if (current >= percent) {
      text.textContent = Math.round(percent) + '%';
      clearInterval(interval);
    } else {
      text.textContent = Math.round(current) + '%';
    }
  }, 25);
}

document.getElementById('startBtn').onclick = async () => {
  const url = document.getElementById('videoUrl').value;
  document.getElementById('status').innerText = '';
  document.getElementById('result').innerText = '';
  document.getElementById('progress').style.width = '0%';
  const resp = await fetch('/process', {
    method: 'POST',
    headers: {'Content-Type':'application/json'},
    body: JSON.stringify({url})
  });
  const { task_id } = await resp.json();
  const evtSrc = new EventSource(`/progress/${task_id}`);
  evtSrc.onmessage = e => {
    const data = JSON.parse(e.data);
    if (!data) return;
    if (data.status === "finished") {
  document.getElementById('status').innerText = "Finished!";
  document.getElementById('result').innerText =
    `Accent: ${data.label}`;
  document.getElementById('progress').style.width = '100%';
  evtSrc.close();
  // Circle:
  let conf = parseFloat(data.confidence.replace('%',''));
  animateConfidenceCircle(conf);
} else {
  document.getElementById('status').innerText =
    data.status.charAt(0).toUpperCase() + data.status.slice(1);
  document.getElementById('progress').style.width =
    (data.progress || 0) + '%';
  // Hide circle during progress
  document.getElementById('circle-container').style.display = 'none';
}
  };
};

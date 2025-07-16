# 🎥 Vid2Story-GenAI

**Vid2Story-GenAI** is a free, offline AI-powered web app that transforms short videos into coherent stories. It uses open-source models for transcription, image captioning, and story generation — with no paid API or OpenAI key required.

---

## ✨ Features

- 📹 Upload a short video
- 🗣️ Transcribe spoken audio using Whisper
- 🖼️ Extract and caption key video frames
- ✍️ Automatically generate a full story from visual and audio content
- 🎭 Choose from genres like horror, comedy, sci-fi, etc.
- 💾 Download the generated story as a text file
- 🧠 All AI runs locally (no paid OpenAI API)

---

## 📦 Tech Stack

| Task                 | Library / Model       |
|----------------------|------------------------|
| Frontend UI          | Streamlit              |
| Audio Transcription  | Whisper (open source)  |
| Image Captioning     | BLIP Base              |
| Story Generation     | GPT-3.5 via `open-source/free model` or offline template |
| Video Frame Extraction | OpenCV               |

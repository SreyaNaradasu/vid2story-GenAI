import streamlit as st
import os
from utils.video_utils import extract_frames, extract_audio
from utils.whisper_transcribe import transcribe
from utils.caption_utils import generate_captions
from utils.story_builder import build_story

st.set_page_config(page_title="Video to Story Generator", layout="centered")

st.markdown(
    "<h1 style='text-align: center;'>🎬 Video to Story Generator</h1>"
    "<p style='text-align: center;'>Upload a short video and watch it become a story using AI!</p>",
    unsafe_allow_html=True
)

video = st.file_uploader("Upload a short video file", type=["mp4", "mov", "avi"])

if video:
    os.makedirs("uploads", exist_ok=True)
    video_path = os.path.join("uploads", "video.mp4")
    with open(video_path, "wb") as f:
        f.write(video.read())

    st.info("🔄 Extracting frames & audio...")
    extract_frames(video_path)
    extract_audio(video_path)

    st.info("🧠 Transcribing audio...")
    transcript = transcribe("uploads/audio.wav")
    st.success("✔️ Transcription complete.")

    st.info("🖼️ Generating image captions...")
    captions = generate_captions()
    st.success("✔️ Image captioning done.")

    st.info("📖 Creating story using GPT-4...")
    story = build_story(captions, transcript)

    st.markdown("### 📝 Generated Story")
    st.text_area("Story", story, height=300)

    with open("outputs/story.txt", "w") as f:
        f.write(story)

    st.download_button("📥 Download Story", story, file_name="story.txt")

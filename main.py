
from fastapi import FastAPI
from pydantic import BaseModel
import subprocess

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/generate")
def generate_video(request: TextRequest):
    # Chama o script para gerar o vídeo e áudio
    subprocess.run(["python3", "stable_video_diffusion.py", "--prompt", request.text])
    subprocess.run(["python3", "bark_tts.py", "--text", request.text])
    
    # Processa o vídeo e salva o arquivo final
    subprocess.run(["python3", "combine_video_audio.py"])

    return {"message": "Video generated successfully", "video_path": "output/final_video.mp4"}

@app.get("/")
def read_root():
    return {"message": "Welcome to DreamClip.AI API!"}

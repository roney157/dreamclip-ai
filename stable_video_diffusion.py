
import os
import imageio
from PIL import Image

def generate_frames(prompt, frame_count=30):
    os.makedirs("frames", exist_ok=True)
    for i in range(frame_count):
        img = Image.new("RGB", (512, 512), (i * 8 % 255, i * 5 % 255, i * 3 % 255))
        img.save(f"frames/frame_{i:03}.png")

def create_video(output_path="output/video.mp4"):
    frames = [imageio.imread(f"frames/frame_{i:03}.png") for i in range(len(os.listdir("frames")))]
    imageio.mimwrite(output_path, frames, fps=8)

if __name__ == "__main__":
    generate_frames("Beautiful sunset over the ocean.")
    create_video("output/video.mp4")

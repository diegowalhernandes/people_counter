from fastapi import FastAPI, UploadFIle, UploadFIle
from fastapi.response import JSONResponse
from app.video_processing import process_video
import os

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exit_ok=True)


@app.post("/uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload/")
async def uplado_video(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    result = process_video(file_path)

    return JSONResponse(content=result)
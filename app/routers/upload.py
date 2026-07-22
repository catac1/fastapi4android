import os
from fastapi import APIRouter, Form, File, UploadFile
from pathlib import Path
from uuid import uuid4


router = APIRouter(prefix="/api/upload", tags=["업로드"])

BASE_DIR = Path(__file__).resolve().parent.parent / Path("images")

#http://서버주소:8000/api/upload/save
#code: 상품코드, image: 업로드할 이미지 파일

@router.post("/save")
async def save_image(code: str = Form(...), image: UploadFile = File (...)):
    # 1. 확장자 추출
    ext = Path(image.filename).suffix
    # 2. 새 파일명 생성 (UUID + 확장자)
    new_filename = f"{uuid4().hex}{ext}"
    # 3. 파일저장 경로
    file_path = BASE_DIR / new_filename
    # 4. 파일저장
    with open(file_path, "wb") as f:
        f.write(await image.read())
    # 5. 응답반환
    return { "result": 1, "code": code, "filename": new_filename}
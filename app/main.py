from fastapi import FastAPI
from app.routers.upload import router as upload_router
from app.routers.mqtt import router as mqtt_router

app = FastAPI()
app.include_router(upload_router)
app.include_router(mqtt_router)
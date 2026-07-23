from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


router = APIRouter(prefix="/mqtt", tags=["mqtt"])

templates = Jinja2Templates(directory="app/templates")


@router.get("/")
async def chat(request: Request):
    return templates.TemplateResponse(request, "mqtt.html", context={})
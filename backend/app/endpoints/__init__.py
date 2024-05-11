from fastapi import APIRouter

api_router = APIRouter(
    prefix="/api",
)

from . import entry_event, event, guest, registration

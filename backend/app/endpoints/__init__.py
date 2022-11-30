from fastapi import APIRouter

api_router = APIRouter(
    prefix="/api",
)

from . import event, guest, entry_event, registration

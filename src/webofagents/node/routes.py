from fastapi import APIRouter
from webofagents.core.models import Handshake

router = APIRouter()

@router.get("/", response_model=Handshake)
async def get_spec_sheet():
    """Returns the specification sheet for an agent."""
    return {
        "title": "AI Agents Collaboration Network",
        "version": "1.0",
        "description": "A modular platform for AI agents to communicate and collaborate effectively."
    }

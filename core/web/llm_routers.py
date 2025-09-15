from fastapi import APIRouter

from core.model.model import llm

router = APIRouter(prefix="/llm", tags=["llm"])

@router.post("/")
async def root(content: str):
    return llm.get_llm_response(content)

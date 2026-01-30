from pydantic import BaseModel
from typing import Optional


class TextPrompt(BaseModel):
    """Schema for text generation requests"""
    text: str
    max_tokens: Optional[int] = 100
    temperature: Optional[float] = 0.7
    top_p: Optional[float] = 0.95


class TextResponse(BaseModel):
    """Schema for text generation responses"""
    generated_text: str
    model: str
    prompt: str


class HealthResponse(BaseModel):
    """Schema for health check responses"""
    status: str
    message: str

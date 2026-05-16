from __future__ import annotations

from pydantic import BaseModel, Field


class CaptureRequest(BaseModel):
    text: str = Field(min_length=1)
    source: str = Field(default="manual", min_length=1)


class ConnectRequest(BaseModel):
    days: int = Field(default=7, ge=1)
    limit: int = Field(default=5, ge=1)


class BriefRequest(BaseModel):
    topic: str = Field(min_length=1)


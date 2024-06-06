from pydantic import BaseModel, Field


class EpisodeCreate(BaseModel):
    id: int = Field(..., title="ID")
    name: str = Field(..., title="Name")
    air_date: str = Field(..., title="Air date")
    episode: str = Field(..., title="Epsode")
    characters: list = Field(..., title="Characters")
    url: str = Field(..., title="URL")
    created: str = Field(..., title="Created")

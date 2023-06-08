import datetime
import uuid

import pydantic


class GdsCase(pydantic.BaseModel):
    id: uuid.UUID
    name: str
    description: str
    difficulty: str
    created_at: datetime.datetime
    grounding: bytes

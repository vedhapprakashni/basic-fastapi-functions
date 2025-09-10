from datetime import datetime, timedelta

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

app = FastAPI()


class Event(BaseModel):
    time: datetime
    user: str
    action: str
    uri: str


def query_events(start_time: datetime):
    """Dummy query for events."""
    time = start_time
    for _ in range(10):
        time += timedelta(seconds=19)
        event = Event(
            time=time,
            user='elliot',
            action='read',
            uri='file:///etc/passwd',
        )
        yield event.model_dump_json() + '\n'


@app.get('/events')
async def get_gen(start: datetime):
    events = query_events(start)
    return StreamingResponse(events)

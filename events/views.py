# Ninja
from ninja import Router
from ninja.errors import HttpError

# Django
from django.http import HttpRequest, HttpResponse

# Local
from events.models import Events
from clients.models import Client
from events.schemas import EventsSchema
from settings.base import logger


event_router = Router()


@event_router.post(path="events/")
async def create_event(
    request: HttpRequest, schema: EventsSchema, response: HttpResponse
):
    client: Client = await Client.objects.aget(telegram_id=schema.client)
    try:
        schema.client = client
        event: Events = await Events.objects.acreate(**schema.dict())
    except Exception as e:
        error_message = (
            "Cannot create event for client client_id "
            f"{schema.client}. ERROR: {e}"
        )
        logger.error(error_message)
        raise HttpError(status_code=409, message=error_message)
    response.status_code = 200
    response.content = (
        f"Event for client {event.client} has been created!"
    )
    return response

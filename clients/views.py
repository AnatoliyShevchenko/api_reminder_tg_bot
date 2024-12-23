# Ninja
from ninja import Router
from ninja.errors import HttpError

# Django
from django.http import HttpRequest, HttpResponse

# Local
from clients.models import Client
from clients.schemas import ClientSchema
from settings.base import logger


client_router = Router()


@client_router.post(path="clients/")
async def create_client(
    request: HttpRequest, schema: ClientSchema, response: HttpResponse
):
    try:
        client: Client = await Client.objects.acreate(**schema.dict())
    except Exception as e:
        error_message = (
            "Cannot create client with telegram_id "
            f"{schema.telegram_id}. ERROR: {e}"
        )
        logger.error(error_message)
        raise HttpError(status_code=409, message=error_message)
    response.status_code = 200
    response.content = f"Client with telegram_id {client.telegram_id} has been created!"
    return response

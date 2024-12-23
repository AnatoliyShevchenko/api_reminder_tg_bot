# Ninja
from ninja import ModelSchema

# Local
from clients.models import Client


class ClientSchema(ModelSchema):
    class Meta:
        model = Client
        fields = ["username", "telegram_id", "timezone"]

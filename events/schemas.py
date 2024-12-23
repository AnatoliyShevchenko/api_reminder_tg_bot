# Ninja
from ninja import ModelSchema

# Local
from events.models import Events


class EventsSchema(ModelSchema):
    class Meta:
        model = Events
        fields = ["client", "title", "description", "execute_at"]

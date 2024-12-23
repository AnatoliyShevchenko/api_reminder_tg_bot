# Ninja
from ninja import NinjaAPI

# Local
from clients.views import client_router
from events.views import event_router


api = NinjaAPI(title="Reminder TG Bot API")
api.add_router(prefix="/", router=client_router)
api.add_router(prefix="/", router=event_router)

# Django
from django.contrib import admin

# Local
from events.models import Events


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    """Admin panel for the client's events."""

    list_display = ("client_id", "title", "created_at", "execute_at")
    search_fields = ("client_id", "title", "created_at", "execute_at")

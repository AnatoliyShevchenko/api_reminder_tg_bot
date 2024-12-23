# Django
from django.contrib import admin

# Local
from clients.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """Admin Panel for the Clients."""

    list_display = (
        "username",
        "telegram_id",
        "timezone",
        "is_superuser",
        "registered_at",
    )
    search_fields = ("username", "telegram_id", "registered_at")

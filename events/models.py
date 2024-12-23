# Django
from django.db import models

# Local
from clients.models import Client


class Events(models.Model):
    """Model for the Client's events."""

    client = models.ForeignKey(
        to=Client,
        on_delete=models.CASCADE,
        to_field="telegram_id",
        related_name="client_events",
        verbose_name="клиент",
    )
    title = models.CharField(verbose_name="заголовок")
    description = models.TextField(
        verbose_name="описание", max_length=500
    )
    created_at = models.DateTimeField(
        verbose_name="создано", auto_now_add=True
    )
    execute_at = models.DateTimeField(verbose_name="выполнить в")

    class Meta:
        ordering = ("-id",)
        verbose_name = "событие"
        verbose_name_plural = "события"

    def __str__(self):
        return f"{self.client} | {self.title} | {self.created_at}"

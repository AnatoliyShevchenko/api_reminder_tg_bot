from __future__ import annotations

# Django
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models

# Local
from settings.base import logger


class ClientManager(BaseUserManager):
    """Manager for the Client."""

    def create_user(self, telegram_id: int, timezone: str) -> Client:
        """Create client method."""
        if not telegram_id:
            raise ValueError("The telegram_id field must be set")
        client: Client = self.model(
            telegram_id=telegram_id, timezone=timezone
        )
        client.save(using=self._db)
        return client

    def create_superuser(self, username: str, password: str) -> Client:
        """Create administrator method."""
        if not username or not password:
            raise ValueError(
                "Fields 'Telegram_id' and 'Password' are required!"
            )
        client: Client = self.model(username=username)
        client.is_active = True
        client.is_staff = True
        client.is_superuser = True
        client.set_password(raw_password=password)
        client.save(using=self._db)
        return client


class Client(AbstractBaseUser, PermissionsMixin):
    """Model for the Client."""

    username = models.CharField(
        verbose_name="имя пользователя",
        unique=True,
        max_length=32,
        blank=True,
        null=True,
    )
    telegram_id = models.PositiveBigIntegerField(
        unique=True,
        verbose_name="id телеграм",
        primary_key=True,
        default=0,
    )
    timezone = models.CharField(
        verbose_name="часовой пояс(utc)", default="UTC+05:00"
    )
    password = models.CharField(
        verbose_name="пароль", max_length=256, blank=True, null=True
    )
    is_active = models.BooleanField(
        verbose_name="активный", default=False
    )
    is_staff = models.BooleanField(
        verbose_name="менеджер", default=False
    )
    is_superuser = models.BooleanField(
        verbose_name="администратор", default=False
    )
    registered_at = models.DateTimeField(
        verbose_name="дата регистрации", auto_now_add=True
    )

    objects = ClientManager()

    USERNAME_FIELD = "username"

    class Meta:
        ordering = ("-telegram_id",)
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self) -> str:
        return (
            f"{self.username} | {self.telegram_id} | "
            f"{self.registered_at} | {self.is_superuser}"
        )

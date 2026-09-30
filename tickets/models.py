from django.conf import settings
from django.db import models

class Ticket(models.Model):
    class Category(models.TextChoices):
        HARDWARE = "HARDWARE", "Hardware"
        SOFTWARE = "SOFTWARE", "Software"
        NETWORK = "NETWORK", "Rede"
        ACCESS = "ACCESS", "Acesso"
        OTHER = "OTHER", "Outro"

    class Priority(models.TextChoices):
        LOW = "LOW", "Baixa"
        MEDIUM = "MEDIUM", "Média"
        HIGH = "HIGH", "Alta"
        CRITICAL = "CRITICAL", "Crítica"

    class Status(models.TextChoices):
        OPEN = "OPEN", "Aberto"
        IN_PROGRESS = "IN_PROGRESS", "Em atendimento"
        RESOLVED = "RESOLVED", "Resolvido"
        CLOSED = "CLOSED", "Fechado"

    title = models.CharField(max_length=200)
    description = models.TextField()

    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.OTHER,
    )
    priority = models.CharField(
        max_length=20,
        choices=Priority.choices,
        default=Priority.MEDIUM,
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.OPEN,
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tickets",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["status"]),
            models.Index(fields=["priority"]),
            models.Index(fields=["category"]),
        ]

    def __str__(self):
        return f"#{self.pk} - {self.title}"

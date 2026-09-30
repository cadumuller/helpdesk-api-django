from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Ticket

class TicketApiTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="carlos",
            password="SenhaForte123!",
        )
        self.other_user = User.objects.create_user(
            username="outro",
            password="SenhaForte123!",
        )
        self.client.force_authenticate(user=self.user)

    def test_create_ticket(self):
        payload = {
            "title": "Sem acesso ao sistema",
            "description": "Usuário recebe erro ao efetuar login.",
            "category": "ACCESS",
            "priority": "HIGH",
            "status": "OPEN",
        }

        response = self.client.post("/api/tickets/", payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ticket.objects.count(), 1)
        self.assertEqual(Ticket.objects.first().created_by, self.user)

    def test_user_only_sees_own_tickets(self):
        Ticket.objects.create(
            title="Chamado do usuário",
            description="Meu chamado",
            created_by=self.user,
        )
        Ticket.objects.create(
            title="Chamado de outro usuário",
            description="Outro chamado",
            created_by=self.other_user,
        )

        response = self.client.get("/api/tickets/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(
            response.data["results"][0]["title"],
            "Chamado do usuário",
        )

    def test_filter_by_status(self):
        Ticket.objects.create(
            title="Aberto",
            description="Teste",
            status="OPEN",
            created_by=self.user,
        )
        Ticket.objects.create(
            title="Resolvido",
            description="Teste",
            status="RESOLVED",
            created_by=self.user,
        )

        response = self.client.get("/api/tickets/?status=RESOLVED")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["status"], "RESOLVED")

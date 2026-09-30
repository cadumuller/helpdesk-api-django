from rest_framework import viewsets

from .filters import TicketFilter
from .models import Ticket
from .permissions import IsOwnerOrStaff
from .serializers import TicketSerializer

class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    permission_classes = [IsOwnerOrStaff]
    filterset_class = TicketFilter
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "updated_at", "priority", "status"]
    ordering = ["-created_at"]

    def get_queryset(self):
        queryset = Ticket.objects.select_related("created_by")

        if self.request.user.is_staff:
            return queryset

        return queryset.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

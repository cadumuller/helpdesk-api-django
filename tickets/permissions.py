from rest_framework.permissions import BasePermission

class IsOwnerOrStaff(BasePermission):
    """
    Usuários comuns só podem alterar/excluir seus próprios chamados.
    Staff pode acessar todos.
    """

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.created_by == request.user

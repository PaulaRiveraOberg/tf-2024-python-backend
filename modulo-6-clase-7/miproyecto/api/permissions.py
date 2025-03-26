from rest_framework.permissions import BasePermission, DjangoModelPermissions


class DjangoModelPermissionsWithView(DjangoModelPermissions):
    perms_map = {
        # sobreescribe el perms_map de DjangoModelPermissions
        # agrega el permiso 'view_%(model_name)s' a los permisos de 'GET'
        "GET": ["%(app_label)s.view_%(model_name)s"],
        "OPTIONS": [],
        "HEAD": [],
        "POST": ["%(app_label)s.add_%(model_name)s"],
        "PUT": ["%(app_label)s.change_%(model_name)s"],
        "PATCH": ["%(app_label)s.change_%(model_name)s"],
        "DELETE": ["%(app_label)s.delete_%(model_name)s"],
    }


class CanEditOwnPostPermission(BasePermission):
    """
    Permiso personalizado para verificar si el usuario tiene el permiso 'change_own_post' en un modelo.
    """

    def has_permission(self, request, view):
        # Verifica si el usuario está autenticado
        if not request.user or not request.user.is_authenticated:
            return False

        # Si el usuario es superusuario, tiene acceso
        if request.user.is_superuser:
            return True

        # Verificar permiso a nivel de modelo (global)
        return request.user.has_perm("miapp.change_own_post")

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

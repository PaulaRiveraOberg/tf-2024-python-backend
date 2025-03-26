from miapp.models import Post
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from .permissions import CanEditOwnPostPermission, DjangoModelPermissionsWithView
from .serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [DjangoModelPermissionsWithView]


class MyPostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [CanEditOwnPostPermission]

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)

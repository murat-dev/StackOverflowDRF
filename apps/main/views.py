from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from apps.main.permissions import IsAuthorPermission
from apps.main.serializers import ProblemCreateSerializer, ReplySerializer, ImageSerializer, CommentSerializer
from apps.main.models import Problem, Reply, CodeImage, Comment


class PermissionMixin:
    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsAuthenticated, ]
        elif self.action in ['update', 'partial_update', 'delete']:
            permissions = [IsAuthorPermission, ]
        else:
            permissions = []
        return [perm() for perm in permissions]

    def get_serializer_context(self):
        return {'request': self.request, 'action': self.action}


class ProblemViewSet(PermissionMixin, viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemCreateSerializer


class ProblemImagesViewSet(viewsets.ModelViewSet):
    queryset = CodeImage.objects.all()
    serializer_class = ImageSerializer



class ReplyViewSet(PermissionMixin, viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer


class CommentViewSet(PermissionMixin, viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


#TODO: вьюшки для ответов
#TODO: вьюшки для комментов
#TODO: обновление картинок
#TODO: регистрация
#TODO: активация
#TODO: отправка СМС
#TODO: восстановление пароля


# class ProblemListView(generics.ListAPIView):
#     queryset = Problem.objects.all()
#     serializer_class = ProblemListSerializer
#
#
# class ProblemCreateView(generics.CreateAPIView):
#     queryset = Problem.objects.all()
#     serializer_class = ProblemCreateSerializer
#     permission_classes = [IsAuthenticated]
#
#
#
# class ProblemDetailView(generics.RetrieveAPIView):
#     queryset = Problem.objects.all()
#     serializer_class = ProblemDetailSerializer
#
#
# class ProblemUpdateView(generics.UpdateAPIView):
#     queryset = Problem.objects.all()
#     serializer_class = ProblemUpdateSerializer
#     permission_classes = [ProblemUpdateDeletePermission, ]
#
#
# class ProblemDeleteView(generics.DestroyAPIView):
#     queryset = Problem.objects.all()
#     permission_classes = [ProblemUpdateDeletePermission, ]
#
#





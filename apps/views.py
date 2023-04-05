from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import ListCreateAPIView

from apps.serializers import UserSerializer
from apps.tasks import send_to_gmail
from root.settings import CACHE_TTL, CACHE_KEY


class UsersListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        email = serializer.validated_data['email']
        send_to_gmail.apply_async(
            args=[email],
            countdown=5
        )
        serializer.save(is_active=True)

    """caching with decorator and cache_page"""
    # @method_decorator(cache_page(CACHE_TTL, key_prefix=CACHE_KEY))
    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

    """caching without decorator and manual cache"""
    # def list(self, request, *args, **kwargs):
    #     if users := cache.get(CACHE_KEY):
    #         serializer = self.serializer_class(users, many=True)
    #         return Response(serializer.data)
    #
    #     serializer = self.serializer_class(self.get_queryset(), many=True)
    #     cache.set(CACHE_KEY, serializer.data, CACHE_TTL)
    #     return Response(serializer.data)

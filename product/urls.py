from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import (ProductViewSet,
                    CommentViewSet)


router = SimpleRouter()
router.register('publications', ProductViewSet, 'publications')
router.register('comments', CommentViewSet, 'comments')

urlpatterns = [
    path('', include(router.urls)),
]





from django.urls import path, include
from rest_framework.routers import SimpleRouter
from main.views import (PublicationViewSet, CommentViewSet)


router = SimpleRouter()
router.register('publications', PublicationViewSet, 'publications')
router.register('comment', CommentViewSet, 'comment')

urlpatterns = [
    path('', include(router.urls))
]



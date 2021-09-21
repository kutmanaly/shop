from django.urls import path, include
from rest_framework.routers import SimpleRouter
from product.views import ProductViewSet, CommentViewSet

router = SimpleRouter()
router.register('products', ProductViewSet, 'products')
router.register('comment', CommentViewSet, 'comment')

urlpatterns = [
    path('', include(router.urls))
]

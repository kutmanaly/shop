from django_filters import rest_framework as rest_filters
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from product.models import Product, Comment
from product.permissions import IsAuthor, IsAuthorOrIsAdmin
from product.serializer import (ProductListSerializer,
                                ProductDetailSerializer,
                                CreateProductSerializer,
                                CommentSerializer)
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters


class ProductFilter(filters.FilterSet):
    created_at = filters.DateTimeFromToRangeFilter()

    class Meta:
        model = Product
        fields = ('title', 'created_at')


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer
    permission_classes = [IsAuthorOrIsAdmin]
    filter_backends = [rest_filters.DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['title', 'text']
    ordering_fields = ['created_at', 'title']

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        elif self.action == 'retrieve':
            return ProductDetailSerializer
        return CreateProductSerializer


class CommentViewSet(mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        return [IsAuthor()]

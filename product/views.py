from django_filters import rest_framework as filters
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import *
from rest_framework import filters as rest_filter

from product.models import Product
from main.permissions import IsAuthorOrIsAdmin, IsAuthor
from main.serializers import PublicationListSerializer, PublicationDetailSerializer, CreatePublicationSerializer, \
    CommentSerializer


class ProductFilter(filters.FilterSet):
    created_at = filters.DateTimeFromToRangeFilter()

    class Meta:
        model = Product
        fields = ('title', 'created_at')


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer
    permission_classes = [IsAuthorOrIsAdmin, ]
    filter_backends = [filters.DjangoFilterBackend,
                       rest_filter.SearchFilter,
                       rest_filter.OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['title', 'text']
    ordering_fields = ['created_at', 'title']

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        elif self.action == 'retrieve':
            return ProductDetailSerializer
        return CreateProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request
        status = request.query_params.get('status')
        queryset = queryset.filter(status=status)
        if status is not None:
            queryset = queryset.filter(status=status)
        return status

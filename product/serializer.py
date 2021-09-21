from rest_framework import serializers
from product.models import Product, Comment


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        return rep


class CommentSerializer(serializers.ModelSerializer):
    publication = serializers.PrimaryKeyRelatedField(write_only=True,
                                                     queryset=Product.objects.all())
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'title', 'text', 'user',)


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        return super().create(validated_data)

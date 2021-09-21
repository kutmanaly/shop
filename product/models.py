from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Product(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    text = models.TextField('Текст')
    price = models.IntegerField('Цена')

    created_at = models.DateField("Дата создания", auto_now_add=True)
    updated_at = models.DateField("Дата редактирования", auto_now=True)

    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


class Comment(models.Model):
    publication = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments',
                                    verbose_name='Объявление')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='Автор')
    text = models.TextField('Текст')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.publication} --> {self.user}'


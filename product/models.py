from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


Rating = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
]


class Product(models.Model):
    title = models.CharField('Название', max_length=255)
    text = models.TextField('Текст')
    price = models.IntegerField('Цена')
    image = models.ImageField('картинка')

    created_at = models.DateField("Дата создания", auto_now_add=True)
    updated_at = models.DateField("Дата редактирования", auto_now=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


class Comment(models.Model):
    product = models.ForeignKey(Product,
                                    on_delete=models.CASCADE,
                                    related_name='reviews',
                                    verbose_name='Продукт')
    users = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='comments',
                             verbose_name='Автор')
    text = models.TextField("Текст")
    rating = models.IntegerField('Рейтинг', choices=Rating)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.publication} --> {self.user}'




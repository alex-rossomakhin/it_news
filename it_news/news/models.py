from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class News(models.Model):
    
    title = models.CharField(max_length=128,
                             verbose_name='Заголовок'
                             )
    text = models.TextField(verbose_name='Текст новости'
                            )
    image = models.ImageField(blank=True,
                              verbose_name='Изображение'
                              )
    slug = models.SlugField(unique=True,
                            verbose_name='URL'
                            )
    pub_data = models.DateTimeField('Дата публикации',
                                    auto_now_add=True
                                    )
    author = models.ForeignKey(User, 
                               on_delete=models.CASCADE,
                               related_name='author_news',
                               verbose_name='Автор'
                               )
    class Meta:
        ordering = ['-pub_data']
        verbos_name = 'Новость'


class Comment(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='author_comment',
                               verbose_name='Автор комментария'
                               )
    news = models.ForeignKey(News,
                             on_delete=models.CASCADE,
                             related_name='comment_news',
                             verbose_name='Комментарий новости'
                             )
    text = models.TextField(max_length=300)
    pub_data = models.DateTimeField('Дата публикации',
                                    auto_now_add=True
                                    )

    def __str__(self):
        return self.author


from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    """Новости """
    subject = models.CharField(verbose_name='заголовок публикации', max_length=256)
    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.SET_NULL, null=True, related_name='article')
    content = models.TextField(verbose_name='текстовый контент')
    date = models.DateTimeField(verbose_name='дата публикации', default=timezone.now)

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-date']

    def __str__(self):
        return '%s %s' % (self.id, self.subject)

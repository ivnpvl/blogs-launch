from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Название',
        help_text='Введите название группы.',
        error_messages={
            'max_lenght': 'Название группы не должно превышать 200 символов.',
            'unique': 'Группа с таким названием уже существует.',
        },
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Уникальный идентификатор',
        help_text=(
            'Введите идентификатор, который будет частью URL страницы. '
            'Допустимо использование латинских букв, символ тире '
            'и нижнее подчёркивание.'
        ),
        error_messages={
            'unique': 'Группа с таким идентификатором уже существует.',
        },
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text=(
            'Добавьте полное описание группы, чтобы вам было проще найти '
            'единомышленников.'
        ),
    )

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(
        verbose_name='Текст публикации',
        help_text='Всё, чем хотите поделиться!'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор публикации',
        help_text='Выберите автора публикации',
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True,
        verbose_name='Группа публикации',
        help_text=(
            'Укажите к какой группе относится публикация. '
            'Оставьте пустым, если подходящей группы нет.'
        ),
    )

    class Meta:
        ordering = ['-pub_date']

import datetime

from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(
        "tag's name",
        max_length=20,
        help_text='max length 20 chars'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['name']


class Article(models.Model):
    title = models.CharField(
        'Title',
        max_length=50,
        help_text='50 chars maximum',
    )
    content = models.TextField(
        'Content',
        help_text='no limited',
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='articles',
    )
    image = models.ImageField(
        'Image',
        width_field=1920,
        height_field=1080,
    )

    pub_date = models.DateField(
        'Date',
        default=datetime.datetime.now,
    )

    slug = models.SlugField(
        'Slug',
        max_length=200,
        unique=True,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail_url', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ('pub_date', 'title')


class Comment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    content = models.TextField(
        'Content',
        help_text='no limited'
    )
    pub_date = models.Model(
        'Date',

    )
    pub_time = models.TimeField(
        'Time',
        default=datetime.datetime.now
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.user}, {self.article.title}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ('pub_date', 'pub_time')


class Like(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    pub_date = models.DateField(
        'Date',
        default=datetime.datetime.now
    )

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
        ordering = ['pub_date']

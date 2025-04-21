from django.db import models

class Categories(models.Model):
    name = models.CharField(
        max_length=30, 
        verbose_name="Название категории"
        )
    slug = models.SlugField(
        verbose_name="Ссылка на категорию", 
        unique=True
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Post(models.Model):
    title = models.CharField(
        max_length=50, 
        verbose_name="Названия поста"
        )
    content = models.TextField(
        null=True, 
        verbose_name="Контент"
        )
    views = models.IntegerField(
        verbose_name="Просмотры", 
        default=0
        )
    published = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Дата публикации"
        )
    categories = models.ForeignKey(
        Categories, 
        verbose_name="Категория поста", 
        on_delete=models.CASCADE
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


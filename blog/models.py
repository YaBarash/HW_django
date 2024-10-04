from django.db import models

from users.models import User


class Blog(models.Model):
    # заголовок, slug, содержимое, превью, дата создания, признак публикации, количество просмотров
    # создаем поля и прописываем их параметры
    title = models.CharField(
        max_length=100,
        verbose_name="заголовок",
        help_text="введите название заголовка",
    )
    slug = models.CharField(
        max_length=100,
        verbose_name="Идентификатор",
        unique=True,
        null=True,
    )
    content = models.TextField(
        max_length=100, verbose_name="содержимое", help_text="Введите содержимое"
    )
    preview = models.ImageField(
        upload_to="catalog/image",
        blank=True,
        null=True,
        verbose_name="изображение",
        help_text="загрузите изображение"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="дата создания",
        help_text="Укажите дату создания"
    )
    published = models.BooleanField(
        default=False,
        verbose_name="публикация",
        help_text="поставьте галочку если статья опубликована"
    )
    views = models.IntegerField(
        default=0,
        verbose_name="Количество просмотров",
        help_text="Укажите количество просмотров"
    )
    user = models.ForeignKey(User, verbose_name="Пользователь", help_text="Укажите пользователя", blank=True, null=True,
                             on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Запись в блоге"
        verbose_name_plural = "Записи в блоге"

        # permissions = [
        #     ('set_published', 'Can publish products'),
        #     ('change_description', 'Can change description'),
        #     ('change_category', 'Can change category'),
        # ]

    # строковое представление объекта
    def __str__(self):
        return f"{self.title}"


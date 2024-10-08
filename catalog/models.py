from django.db import models

from users.models import User


# Create your models here.


# создаем модель категории как одного ко многим
class Category(models.Model):
    # наименование, описание
    name = models.CharField(
        max_length=100, verbose_name="категория", help_text="Введите категорию продукта"
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории продукта",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.name} {self.description}"


# создаем модель продуктов как многих к одной категории. Ссылка на категорию
# создаем класс и наследуемся от models.Model
class Product(models.Model):
    # имя, порода, фото, дата рождения
    # создаем поля и прописываем их параметры
    name = models.CharField(
        max_length=100,
        verbose_name="наименование",
        help_text="введите наименование продукта",
    )
    description = models.TextField(
        max_length=100, verbose_name="описание", help_text="Введите описание продукта"
    )
    image = models.ImageField(
        upload_to="catalog/image",
        blank=True,
        null=True,
        verbose_name="изображение",
        help_text="загрузите изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="введите категорию продукта",
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.PositiveIntegerField(default=0, )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name="дата создания",
        help_text="Укажите дату создания записи в БД",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="дата последнего изменения",
        help_text="Укажите дату изменения записи в БД",
    )
    user = models.ForeignKey(User, verbose_name="Пользователь", help_text="Укажите пользователя", blank=True, null=True,
                             on_delete=models.SET_NULL)
    publication = models.BooleanField(default=False, verbose_name="признак публикации продукта", help_text="продукт опубликован")

    # Класс мета
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name"]

        permissions = [
            ('set_published', 'Can publish products'),
            ('change_description', 'Can change description'),
            ('change_category', 'Can change category'),
        ]

    # строковое представление объекта
    def __str__(self):
        return f"{self.name} {self.category} {self.created_at}"

from django.db import models


class Type(models.Model):
    name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        verbose_name='Тип задачи'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип задачи'
        verbose_name_plural = 'Типы задач'

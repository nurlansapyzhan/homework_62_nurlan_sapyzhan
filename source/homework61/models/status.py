from django.db import models


class Status(models.Model):
    name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        verbose_name='Статус задачи'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

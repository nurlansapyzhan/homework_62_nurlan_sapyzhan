from django.db import models


class Project(models.Model):
    start_date = models.DateField(
        verbose_name='Дата начала',
        null=False
    )
    end_date = models.DateField(
        verbose_name='Дата окончания',
        null=True
    )
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Название'
    )
    description = models.TextField(
        max_length=254,
        null=True,
        verbose_name='Описание'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

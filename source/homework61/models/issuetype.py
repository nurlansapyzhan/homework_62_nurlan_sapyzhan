from django.db import models


class IssueType(models.Model):
    issue = models.ForeignKey(
        'homework61.Issue',
        related_name='issue_types',
        on_delete=models.PROTECT,
        verbose_name='Задача'
    )
    type = models.ForeignKey(
        'homework61.Type',
        related_name='type_issues',
        on_delete=models.PROTECT,
        verbose_name='Тип'
    )

    def __str__(self):
        return f'{self.issue} - {self.type}'

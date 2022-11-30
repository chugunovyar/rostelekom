from django.db import models
from django.utils import timezone


class Appeal(models.Model):
    description = models.TextField(verbose_name='текст обращения')
    client = models.ForeignKey(
        'Client',
        verbose_name='клиент',
        related_name='appeals',
        on_delete=models.CASCADE,
     )
    created = models.DateField(verbose_name='дата создания', auto_now_add=True)

    class Meta:
        ordering = ["-created"]
    def __str__(self):
        return f'{(self.created)}'

class Client(models.Model):
    name = models.CharField('имя', max_length=200)
    surname = models.CharField('фамилия', max_length=200, blank=True)
    patronymic = models.CharField('отчество', max_length=200, blank=True)
    phone = models.CharField('телефон', max_length=200)

    def __str__(self):
        return f'{self.name} {self.surname}'    
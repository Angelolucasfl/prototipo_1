from django.db import models
from django.core.exceptions import ValidationError

def validate_float_range(value):
    if value < 0.0 or value > 10.0:
        raise ValidationError('O valor deve estar entre 0.0 e 10.0')


class Filme(models.Model):
    nome = models.CharField(max_length=200)
    nota = models.FloatField(
        validators=[validate_float_range],
        default=0.0
    )
    ano = models.IntegerField()
    sinopse = models.TextField(blank=True)
    genero = models.CharField(max_length=500)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.nome = self.nome.capitalize()
        super().save(*args, **kwargs)

from django.contrib.auth.models import User
from django.db import models


class Jogador(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  xp = models.PositiveIntegerField(default=0,
                                   verbose_name="Pontos de Experiência")
  level = models.PositiveIntegerField(default=1)
  titulo = models.CharField(max_length=100,
                            blank=True,
                            null=True,
                            default="Aventureiro Novato")

  def __str__(self):
    return self.user.username

from django.db import models

# Create your models here.
class Fact(models.Model):
    descricao = models.CharField(max_length=200)
    curtidas = models.IntegerField(default=0)

    


    
from django.db import models

class indiceDB(models.Model):
    titulo = models.CharField(max_length=30)
    serie = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    editor = models.CharField(max_length=30)
    idioma = models.CharField(max_length=30)
    pag = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    formato = models.CharField(max_length=30)
    genero= models.CharField(max_length=30)

def __str__(self):
    return "%s %s"%(self.titulo, self.serie)




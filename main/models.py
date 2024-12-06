from django.db import models

class Yonalish(models.Model):
    nom = models.CharField(max_length=50)
    aktiv = models.CharField(max_length=50)

    def __str__(self):
        return self.nom
    class Meta:
        verbose_name_plural = 'Yonalishlar'

class Fan(models.Model):
    nom = models.CharField(max_length=50)
    yonalish = models.ForeignKey(Yonalish, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name_plural = 'Fanlar'
class Ustoz(models.Model):
    ism = models.CharField(max_length=50)
    jins = models.CharField(max_length=50,choices=(("Erkak","Erkak"),("Ayol","Ayol")))
    yosh = models.PositiveSmallIntegerField()
    daraja = models.CharField(max_length=50,choices=(('Bakalavr','Bakalavr'),('Magistr','Magistor'),('Doktor','Doktor')))
    fan = models.ForeignKey(Fan, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.ism
    class Meta:
        verbose_name_plural = 'Ustozlar'


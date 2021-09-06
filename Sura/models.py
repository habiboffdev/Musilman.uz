from django.db import models

# Create your models here.
class Sura(models.Model):
    surah_name = models.CharField(max_length=150)
    surah_r_city = models.CharField(max_length=150)
    surah_number = models.CharField(max_length=150)
    surah_ayahs_number = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.surah_name
class Ayah(models.Model):
    surah = models.ForeignKey(
        Sura,
        on_delete=models.CASCADE,
    )
    ayah_number = models.PositiveIntegerField()
    ayah_text = models.TextField()
    audio_url= models.URLField()
    
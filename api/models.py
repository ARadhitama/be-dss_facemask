from django.db import models

class Camera(models.Model):
    lokasi = models.CharField(max_length=20)

class Pengunjung(models.Model):
    kamera = models.ForeignKey(
        Camera,
        on_delete=models.CASCADE
    )
    melanggar = models.BooleanField(default=False)
    waktu = models.DateTimeField(auto_now_add=True)

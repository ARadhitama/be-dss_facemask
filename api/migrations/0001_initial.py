# Generated by Django 3.0.4 on 2020-11-27 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lokasi', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pengunjung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('melanggar', models.BooleanField(default=False)),
                ('waktu', models.DateTimeField(auto_now_add=True)),
                ('kamera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Camera')),
            ],
        ),
    ]

# Generated by Django 3.2 on 2022-08-19 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0003_auto_20220817_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(default='noticias/default.jpg', upload_to='noticias'),
        ),
    ]

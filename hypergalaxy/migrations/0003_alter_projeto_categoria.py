# Generated by Django 5.0.2 on 2024-02-18 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hypergalaxy', '0002_projeto_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='categoria',
            field=models.CharField(max_length=50),
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-25 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classifier',
            name='classificationCorrect',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='classifier',
            name='feedback',
            field=models.TextField(null=True),
        ),
    ]

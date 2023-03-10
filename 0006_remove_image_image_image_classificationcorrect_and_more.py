# Generated by Django 4.1.3 on 2022-12-13 02:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0005_remove_image_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='classificationCorrect',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='feedback',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='input_image',
            field=models.TextField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='output_image',
            field=models.BooleanField(),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
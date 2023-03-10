# Generated by Django 4.1.3 on 2022-11-28 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0002_alter_classifier_classificationcorrect_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locator',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('input', models.TextField()),
                ('locOutput', models.TextField()),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='email')),
            ],
        ),
    ]
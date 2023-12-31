# Generated by Django 4.2.4 on 2023-09-04 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('is_done', models.BooleanField(default=False)),
            ],
        ),
    ]

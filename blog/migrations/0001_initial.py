# Generated by Django 4.2.14 on 2024-08-05 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('text', models.CharField(max_length=250)),
            ],
        ),
    ]

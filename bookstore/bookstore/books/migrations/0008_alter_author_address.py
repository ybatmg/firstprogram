# Generated by Django 5.0.2 on 2024-02-13 07:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_alter_author_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='address',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='books.address'),
        ),
    ]
# Generated by Django 5.1.1 on 2024-09-12 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_rename_notes_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='owner',
            field=models.IntegerField(),
        ),
    ]

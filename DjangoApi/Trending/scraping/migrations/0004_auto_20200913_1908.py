# Generated by Django 3.1.1 on 2020-09-13 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0003_googlesearchelement'),
    ]

    operations = [
        migrations.RenameField(
            model_name='googlesearchelement',
            old_name='rank',
            new_name='link',
        ),
    ]

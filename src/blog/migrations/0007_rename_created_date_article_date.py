# Generated by Django 4.0.3 on 2022-03-24 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_article_created_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='created_date',
            new_name='date',
        ),
    ]
# Generated by Django 4.0.3 on 2022-03-24 02:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_article_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

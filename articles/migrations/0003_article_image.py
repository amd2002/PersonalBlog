# Generated by Django 4.2 on 2024-09-02 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_rename_sumary_article_summary_alter_article_date_pub'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='articles_images/'),
        ),
    ]

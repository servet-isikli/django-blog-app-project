# Generated by Django 4.1.7 on 2023-04-02 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_users_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'Blog', 'verbose_name_plural': 'Blogs'},
        ),
    ]

# Generated by Django 5.1.3 on 2024-12-05 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0004_alter_produto_options_alter_produto_scale'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='deadline',
        ),
    ]

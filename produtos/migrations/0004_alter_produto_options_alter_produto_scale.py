# Generated by Django 5.1.3 on 2024-12-05 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_produto_buy_price_produto_description_produto_line_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='produto',
            options={'ordering': ['title']},
        ),
        migrations.AlterField(
            model_name='produto',
            name='scale',
            field=models.CharField(max_length=10),
        ),
    ]

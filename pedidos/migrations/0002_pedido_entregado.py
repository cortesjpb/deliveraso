# Generated by Django 3.0.4 on 2020-04-02 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='entregado',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.0.4 on 2024-06-04 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_remove_cliente_direccion_remove_cliente_emails_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contacto',
        ),
    ]

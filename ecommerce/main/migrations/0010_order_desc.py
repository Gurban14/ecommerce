# Generated by Django 5.1.1 on 2024-11-10 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
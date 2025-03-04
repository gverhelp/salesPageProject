# Generated by Django 5.1.5 on 2025-02-06 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesPage', '0005_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]

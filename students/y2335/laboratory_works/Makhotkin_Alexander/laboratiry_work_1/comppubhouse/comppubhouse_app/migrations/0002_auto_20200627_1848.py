# Generated by Django 3.0.7 on 2020-06-27 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comppubhouse_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='count',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=5),
        ),
        migrations.DeleteModel(
            name='Storage',
        ),
    ]

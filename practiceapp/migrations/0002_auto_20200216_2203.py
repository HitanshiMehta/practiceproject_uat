# Generated by Django 3.0.2 on 2020-02-16 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practiceapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]

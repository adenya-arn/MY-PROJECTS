# Generated by Django 5.1.1 on 2024-09-22 09:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_performance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='classes',
            name='stream',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='school.stream'),
        ),
    ]

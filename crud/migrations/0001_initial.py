# Generated by Django 5.1.2 on 2024-10-15 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='crud',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('first', models.CharField(max_length=40)),
                ('last', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'crud',
            },
        ),
    ]
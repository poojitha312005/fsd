# Generated by Django 5.0.6 on 2024-05-08 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodcat', models.CharField(max_length=200)),
                ('pid', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('cost', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]

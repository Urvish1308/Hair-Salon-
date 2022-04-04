# Generated by Django 4.0.3 on 2022-04-02 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130)),
                ('contact', models.CharField(max_length=13)),
                ('city', models.CharField(max_length=50)),
                ('date', models.DateField()),
            ],
        ),
    ]

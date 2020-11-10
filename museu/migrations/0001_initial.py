# Generated by Django 3.1.2 on 2020-10-29 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Titulo lindo', max_length=140)),
                ('description', models.CharField(default='Uma bela descrição', max_length=280)),
                ('type', models.CharField(default='text', max_length=5)),
                ('media', models.BinaryField(default=b'umaimagembembonita')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]

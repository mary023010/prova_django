# Generated by Django 3.0.1 on 2022-03-25 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Utente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('nome', models.CharField(max_length=200)),
                ('cognome', models.CharField(default='Rossi', max_length=200)),
            ],
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-26 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_familiar', models.CharField(max_length=30)),
                ('edad_familiar', models.IntegerField()),
                ('documento_familiar', models.IntegerField()),
            ],
        ),
    ]

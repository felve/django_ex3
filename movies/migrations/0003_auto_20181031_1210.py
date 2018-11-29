# Generated by Django 2.1.2 on 2018-10-31 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20181028_0033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='mascotas',
            name='estados',
            field=models.ManyToManyField(to='movies.Estados'),
        ),
    ]

# Generated by Django 2.2.7 on 2019-11-18 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=200)),
                ('AuthorFirstName', models.CharField(max_length=100)),
                ('AuthorLastName', models.CharField(max_length=100)),
                ('Price', models.FloatField()),
                ('Quantity', models.IntegerField()),
            ],
        ),
    ]
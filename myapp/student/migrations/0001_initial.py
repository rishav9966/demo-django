# Generated by Django 3.0.2 on 2020-01-19 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.TextField()),
                ('name', models.TextField(max_length=45)),
                ('stud_class', models.TextField()),
                ('department', models.TextField()),
            ],
        ),
    ]

# Generated by Django 3.2.5 on 2021-07-05 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('images', models.ImageField(null=True, upload_to='')),
                ('tag', models.CharField(max_length=20, null=True)),
                ('memo', models.TextField(null=True)),
                ('lat', models.CharField(max_length=30)),
                ('lng', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]

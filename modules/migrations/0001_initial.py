# Generated by Django 4.2.1 on 2023-06-26 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_image', models.FileField(default=None, max_length=500, null=True, upload_to='recipess/')),
                ('recipe_name', models.CharField(max_length=100)),
                ('intro', models.CharField(max_length=1000)),
                ('ingredients', models.CharField(max_length=1000)),
                ('making', models.CharField(max_length=100)),
                ('nut', models.CharField(max_length=100)),
                ('protein', models.CharField(max_length=100)),
            ],
        ),
    ]
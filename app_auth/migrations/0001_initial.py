# Generated by Django 4.0.2 on 2022-02-24 13:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('born', models.IntegerField(default=1900, validators=[django.core.validators.MinValueValidator(1700), django.core.validators.MaxValueValidator(2022)])),
                ('died', models.IntegerField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_auth.author')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'ordering': ['title', 'author'],
            },
        ),
        migrations.AddConstraint(
            model_name='author',
            constraint=models.UniqueConstraint(fields=('last_name', 'first_name'), name='unique author'),
        ),
        migrations.AddConstraint(
            model_name='book',
            constraint=models.UniqueConstraint(fields=('title', 'author'), name='unique book author'),
        ),
    ]

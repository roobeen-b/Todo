# Generated by Django 4.0 on 2022-01-03 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('created', models.DateField(default='2022-01-03')),
                ('dueDate', models.DateField(default='2022-01-03')),
                ('category', models.ForeignKey(default='General', on_delete=django.db.models.deletion.CASCADE, to='todolist.category')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]

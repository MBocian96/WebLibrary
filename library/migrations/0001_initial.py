# Generated by Django 3.1.4 on 2021-01-05 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isnb', models.CharField(max_length=13)),
                ('title', models.CharField(max_length=40)),
                ('author', models.CharField(max_length=40)),
                ('genre', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isnb', models.CharField(max_length=13)),
                ('mark', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=50)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
            ],
        ),
    ]
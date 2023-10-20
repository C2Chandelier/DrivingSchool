# Generated by Django 4.2.6 on 2023-10-17 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('h_total', models.IntegerField(default=0)),
                ('h_remaining', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Planning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('place', models.CharField(max_length=200)),
                ('hour', models.CharField(max_length=200)),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DSchool.instructor')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DSchool.student')),
            ],
        ),
    ]
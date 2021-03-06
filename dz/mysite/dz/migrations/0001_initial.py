# Generated by Django 3.1.4 on 2021-01-12 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discipline_name_txt', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name_text', models.CharField(max_length=20)),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dz.discipline')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name_text', models.CharField(max_length=20)),
                ('birth_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dz.group')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='students',
            field=models.ManyToManyField(to='dz.Student'),
        ),
    ]

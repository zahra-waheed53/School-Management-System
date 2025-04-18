# Generated by Django 5.2 on 2025-04-11 07:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicTerm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('mid', 'Mid'), ('final', 'Final')], max_length=100)),
                ('current', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='AcademicYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('current', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('total_students', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('total_students', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_marks', models.DecimalField(decimal_places=1, max_digits=10)),
                ('obtained_marks', models.DecimalField(decimal_places=1, max_digits=10)),
                ('is_passed', models.BooleanField(default=True)),
                ('rank', models.IntegerField()),
                ('academic_term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='academic_term_results', to='api.academicterm')),
                ('academic_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='academic_year_results', to='api.academicyear')),
            ],
        ),
    ]

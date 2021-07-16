# Generated by Django 3.2.5 on 2021-07-16 11:50

import classbook_core.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('is_admin', models.BooleanField()),
                ('registration_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0)])),
                ('name', models.CharField(max_length=300)),
                ('student_count', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('year_code', models.SmallIntegerField(default=-2, verbose_name=classbook_core.models.Year_Code)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('institution_id', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0)])),
                ('name', models.CharField(max_length=300)),
                ('student_count', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('doc_id', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0)])),
                ('name', models.CharField(max_length=300)),
                ('doc_type', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=300)),
                ('view_count', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('upload_date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classbook_core.appuser')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classbook_core.course')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classbook_core.institution')),
            ],
        ),
        migrations.AddField(
            model_name='appuser',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classbook_core.institution'),
        ),
    ]

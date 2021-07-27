# Generated by Django 3.2.5 on 2021-07-27 09:20

import classbook_core.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('institution', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='classbook_core.institution')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classbook_core.course')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classbook_core.institution')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500, validators=[django.core.validators.MinValueValidator(1)])),
                ('publish_date', models.DateField(auto_now_add=True)),
                ('likes_count', models.IntegerField(default=0)),
                ('associated_document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classbook_core.document')),
                ('auther', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classbook_core.profile')),
                ('replied_to_comment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='classbook_core.comment')),
            ],
        ),
    ]

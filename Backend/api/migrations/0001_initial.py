# Generated by Django 5.1.2 on 2024-10-25 09:40

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.CharField(max_length=20)),
                ('message', models.TextField()),
                ('submitted_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('resume', models.FileField(upload_to='resumes/')),
                ('applied_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serialno', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('experience_level', models.CharField(max_length=50)),
                ('is_immediate_joiner', models.BooleanField(default=False)),
                ('location', models.CharField(max_length=100)),
                ('minimum_qualification', models.CharField(max_length=255)),
                ('additional_requirements1', models.TextField(blank=True, null=True)),
                ('additional_requirements2', models.TextField(blank=True, null=True)),
                ('additional_requirements3', models.TextField(blank=True, null=True)),
                ('additional_requirements4', models.TextField(blank=True, null=True)),
                ('additional_requirements5', models.TextField(blank=True, null=True)),
                ('additional_requirements6', models.TextField(blank=True, null=True)),
                ('additional_requirements7', models.TextField(blank=True, null=True)),
                ('additional_requirements8', models.TextField(blank=True, null=True)),
                ('additional_requirements9', models.TextField(blank=True, null=True)),
                ('additional_requirements10', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
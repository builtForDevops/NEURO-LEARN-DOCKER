# Generated by Django 2.1.7 on 2019-09-28 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20190824_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datasets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_id', models.CharField(max_length=32, unique=True)),
                ('proj_id', models.CharField(max_length=32)),
                ('data_name', models.CharField(max_length=64, unique=True)),
                ('data_cont', models.TextField(max_length=4294967295)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proj_id', models.CharField(max_length=32, unique=True)),
                ('label', models.CharField(max_length=32, unique=True)),
                ('title', models.CharField(max_length=128)),
                ('introduction', models.CharField(max_length=4096)),
                ('methods', models.CharField(max_length=4096)),
                ('flowchart_url', models.CharField(max_length=128)),
                ('workflows_url', models.CharField(max_length=128)),
                ('templates_url', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Submissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=32, unique=True)),
                ('proj_id', models.CharField(max_length=32)),
                ('task_name', models.CharField(max_length=64)),
                ('task_type', models.CharField(max_length=16)),
                ('task_config', models.CharField(max_length=4096)),
                ('task_status', models.CharField(max_length=16)),
                ('task_result', models.TextField(max_length=4294967295)),
            ],
        ),
        migrations.CreateModel(
            name='User_Proj_Auth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=32)),
                ('proj_id', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=32, unique=True)),
                ('username', models.CharField(max_length=16, unique=True)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
    ]

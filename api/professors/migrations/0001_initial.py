# Generated by Django 2.2.17 on 2021-01-26 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('public_id', models.CharField(db_index=True, editable=False, max_length=12, unique=True, verbose_name='public_id')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created date')),
                ('last_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='last modified')),
                ('name', models.TextField(blank=True, help_text='name for professor', null=True, verbose_name='name')),
                ('email', models.EmailField(blank=True, help_text='I stand out in that an e-mail is stored', max_length=254, unique=True, verbose_name='email address')),
            ],
            options={
                'verbose_name': 'Professor',
                'verbose_name_plural': 'Professors',
            },
        ),
    ]
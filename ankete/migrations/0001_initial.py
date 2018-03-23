# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-09 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('value', models.IntegerField()),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('multiansw', models.BooleanField()),
                ('answers', models.ManyToManyField(to='ankete.Answer')),
            ],
        ),
        migrations.AddField(
            model_name='inquiry',
            name='questions',
            field=models.ManyToManyField(to='ankete.Question'),
        ),
    ]

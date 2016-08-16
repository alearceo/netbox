# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-15 19:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('extras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.PositiveSmallIntegerField(choices=[(100, b'Text'), (200, b'Integer'), (300, b'Boolean (true/false)'), (400, b'Date'), (500, b'Selection')], default=100)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('label', models.CharField(blank=True, help_text=b"Name of the field as displayed to users (if not provided, the field's name will be used)", max_length=50)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('required', models.BooleanField(default=False, help_text=b'Determines whether this field is required when creating new objects or editing an existing object.')),
                ('default', models.CharField(blank=True, help_text=b'Default value for the field. N/A for selection fields.', max_length=100)),
                ('obj_type', models.ManyToManyField(help_text=b'The object(s) to which this field applies.', related_name='custom_fields', to='contenttypes.ContentType', verbose_name=b'Object(s)')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CustomFieldChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100)),
                ('weight', models.PositiveSmallIntegerField(default=100)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='extras.CustomField')),
            ],
            options={
                'ordering': ['field', 'weight', 'value'],
            },
        ),
        migrations.CreateModel(
            name='CustomFieldValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obj_id', models.PositiveIntegerField()),
                ('val_int', models.BigIntegerField(blank=True, null=True)),
                ('val_char', models.CharField(blank=True, max_length=100)),
                ('val_date', models.DateField(blank=True, null=True)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='extras.CustomField')),
                ('obj_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ['obj_type', 'obj_id'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='customfieldvalue',
            unique_together=set([('field', 'obj_type', 'obj_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='customfieldchoice',
            unique_together=set([('field', 'value')]),
        ),
    ]
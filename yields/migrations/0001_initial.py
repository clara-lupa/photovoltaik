# Generated by Django 3.1.4 on 2020-12-15 11:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PvYield',
            fields=[
                ('state', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('spec_yield', models.IntegerField()),
            ],
            options={
                'ordering': ['state'],
            },
        ),
    ]

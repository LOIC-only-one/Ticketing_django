# Generated by Django 5.0.4 on 2024-04-21 06:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('priority', models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')])),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('OPEN', 'Open'), ('IN_PROGRESS', 'In Progress'), ('CLOSED', 'Closed')], max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.category')),
            ],
        ),
    ]

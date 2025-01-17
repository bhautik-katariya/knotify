# Generated by Django 5.1.4 on 2025-01-06 11:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inviter', '0002_rename_invitee_inviter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inviter',
            options={'verbose_name': 'Inviter'},
        ),
        migrations.CreateModel(
            name='EventDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_name', models.CharField(max_length=100, verbose_name='Event Name')),
                ('g_name', models.CharField(max_length=50, verbose_name='Groom Name')),
                ('b_name', models.CharField(max_length=50, verbose_name='Bride Name')),
                ('e_date', models.DateTimeField(verbose_name='Event Date')),
                ('place', models.CharField(max_length=500)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inviter.inviter')),
            ],
            options={
                'verbose_name': 'Event Details',
            },
        ),
    ]

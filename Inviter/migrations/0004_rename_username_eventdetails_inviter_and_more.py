# Generated by Django 5.0.6 on 2025-01-12 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Invitee', '0003_alter_invitee_options'),
        ('Inviter', '0003_alter_inviter_options_eventdetails'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventdetails',
            old_name='username',
            new_name='inviter',
        ),
        migrations.AddField(
            model_name='eventdetails',
            name='invitee',
            field=models.ManyToManyField(related_name='event', to='Invitee.invitee'),
        ),
    ]
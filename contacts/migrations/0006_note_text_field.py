# Generated by Django 4.0.3 on 2022-06-28 18:41

from django.db import migrations
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_remove_note_time_published_contact_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='text_field',
            field=localflavor.us.models.USStateField(blank=True, max_length=2, null=True),
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-31 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0003_chaicertificate_chaireview_store'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='chai_variety',
            new_name='chai_varieties',
        ),
    ]

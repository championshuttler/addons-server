# Generated by Django 2.2.6 on 2019-11-01 12:22

from django.db import migrations

from olympia.versions.compare import version_int


def increase_version_int_for_asterisk(apps, schema_editor):
    AppVersion = apps.get_model('applications', 'AppVersion')
    for app in AppVersion.objects.filter(version='*'):
        app.update(version_int=version_int(app.version))


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(increase_version_int_for_asterisk),
    ]

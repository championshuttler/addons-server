# Generated by Django 2.2.6 on 2019-11-07 13:02

from django.db import migrations, models


def set_guid_from_addon(apps, schema_editor):
    Block = apps.get_model('blocklist', 'Block')
    for block in Block.objects.filter(guid=None):
        block.update(guid=block.addon.guid)


class Migration(migrations.Migration):

    dependencies = [
        ('blocklist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='guid',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='include_in_legacy',
            field=models.BooleanField(default=False, help_text='Include in legacy xml blocklist too, as well as new v3'),
        ),
        migrations.RunPython(set_guid_from_addon),
    ]

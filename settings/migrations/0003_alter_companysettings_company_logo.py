# Generated by Django 4.2.3 on 2023-07-26 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_alter_companysettings_company_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companysettings',
            name='company_logo',
            field=models.FileField(default='icon.svg', upload_to='logo/'),
        ),
    ]

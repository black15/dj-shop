# Generated by Django 4.1.4 on 2023-01-02 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_account_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/accounts/images/%Y/%m/%d', verbose_name='User picture'),
        ),
    ]

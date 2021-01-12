# Generated by Django 3.1.3 on 2020-12-31 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20201231_1507'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_email',
            new_name='pro_email',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_address',
            new_name='productOnwer_address',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_bdate',
            new_name='productOnwer_bdate',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_pnumber',
            new_name='productOnwer_pnumber',
        ),
        migrations.AddField(
            model_name='product',
            name='productOnwer_name',
            field=models.CharField(max_length=70, null=True, verbose_name='name'),
        ),
    ]

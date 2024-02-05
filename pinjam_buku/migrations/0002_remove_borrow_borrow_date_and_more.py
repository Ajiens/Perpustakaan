# Generated by Django 5.0 on 2023-12-09 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinjam_buku', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrow',
            name='borrow_date',
        ),
        migrations.RemoveField(
            model_name='borrow',
            name='duration_days',
        ),
        migrations.RemoveField(
            model_name='borrow',
            name='email_address',
        ),
        migrations.RemoveField(
            model_name='borrow',
            name='return_date',
        ),
        migrations.RemoveField(
            model_name='borrow',
            name='telephone_number',
        ),
        migrations.AddField(
            model_name='borrow',
            name='is_dikembalikan',
            field=models.BooleanField(default=False),
        ),
    ]
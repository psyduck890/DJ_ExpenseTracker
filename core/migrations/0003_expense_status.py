# Generated by Django 5.0.4 on 2024-05-08 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_expense_receipt'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('approved', 'approved')], default='pending', max_length=20),
        ),
    ]

# Generated by Django 5.0.4 on 2024-05-08 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_expense_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date_created',
            field=models.DateField(auto_created=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('approved', 'approved'), ('rejected', 'rejected')], default='pending', max_length=20),
        ),
    ]

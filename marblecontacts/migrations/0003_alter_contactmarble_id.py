# Generated by Django 4.2 on 2025-02-13 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marblecontacts', '0002_auto_20230505_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmarble',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

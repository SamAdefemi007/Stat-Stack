# Generated by Django 4.0.3 on 2022-03-26 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('statlist', '0007_alter_transfermarket_contractexpiry'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='playerValue',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='statlist.transfermarket'),
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-26 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statlist', '0005_remove_player_skills_player_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfermarket',
            name='value',
            field=models.CharField(max_length=10, null=True),
        ),
    ]

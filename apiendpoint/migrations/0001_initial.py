# Generated by Django 4.0.4 on 2022-10-28 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slackUsername', models.CharField(max_length=250)),
                ('backend', models.BooleanField(blank=True, default=False, null=True)),
                ('age', models.IntegerField()),
                ('bio', models.TextField()),
            ],
        ),
    ]

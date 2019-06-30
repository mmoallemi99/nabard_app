# Generated by Django 2.2.2 on 2019-06-29 21:40

from django.db import migrations, models
import django.db.models.deletion
import nabard.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_title', models.CharField(max_length=50)),
                ('app_file', models.FileField(upload_to='media/apps/%Y/%m', validators=[nabard.validators.validate_archived_file])),
                ('powerpoint_file', models.FileField(upload_to='media/powerpoints/%Y/%m', validators=[nabard.validators.validate_powerpoint_file])),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nabard.Team')),
            ],
        ),
    ]

# Generated by Django 2.2.7 on 2021-04-17 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0032_status_autostatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlertLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('temptime', models.DateTimeField(auto_now=True)),
                ('comments', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='status',
            old_name='autostatus',
            new_name='lightstatus',
        ),
        migrations.RenameField(
            model_name='status',
            old_name='ledstatus',
            new_name='smokestatus',
        ),
        migrations.RemoveField(
            model_name='status',
            name='alertstatus',
        ),
        migrations.RemoveField(
            model_name='status',
            name='windowclose',
        ),
        migrations.RemoveField(
            model_name='status',
            name='windowopen',
        ),
        migrations.RemoveField(
            model_name='status',
            name='windowstatus',
        ),
        migrations.AddField(
            model_name='status',
            name='smoke',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='status',
            name='smokeset',
            field=models.FloatField(default=0.0),
        ),
    ]

# Generated by Django 2.0.2 on 2018-03-03 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='attribute',
            unique_together={('domain', 'name')},
        ),
        migrations.AlterUniqueTogether(
            name='status',
            unique_together={('domain', 'name')},
        ),
        migrations.AlterModelTable(
            name='attribute',
            table='c_attribute',
        ),
        migrations.AlterModelTable(
            name='domain',
            table='c_domain',
        ),
        migrations.AlterModelTable(
            name='status',
            table='c_status',
        ),
    ]

# Generated by Django 2.0.2 on 2018-03-03 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.Domain')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.Domain')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.Status')),
            ],
        ),
        migrations.AddField(
            model_name='attribute',
            name='domain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.Domain'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.Attribute'),
        ),
    ]

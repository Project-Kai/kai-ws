# Generated by Django 2.1.5 on 2019-01-10 10:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('results', '0001_initial'),
        ('samples', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.Result')),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samples.Sample')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TestType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=25)),
                ('description', models.CharField(blank=True, default='', max_length=50)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='test',
            name='test_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.TestType'),
        ),
    ]

# Generated by Django 2.0.7 on 2018-07-15 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MajorLifeEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('details', models.CharField(max_length=100)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('common_name', models.CharField(max_length=100)),
                ('botanical_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('is_toxic', models.BooleanField(default=False)),
                ('longevity', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=50)),
                ('source', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlantGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='plant',
            name='plant_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plants', to='plantlist.PlantGroup'),
        ),
        migrations.AddField(
            model_name='majorlifeevent',
            name='plant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='life_events', to='plantlist.Plant'),
        ),
    ]
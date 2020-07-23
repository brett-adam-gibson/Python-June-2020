# Generated by Django 2.2.13 on 2020-07-23 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0003_auto_20200713_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wedding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wedder_one', models.CharField(max_length=255)),
                ('wedder_two', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('guests', models.ManyToManyField(related_name='weddings_attending', to='home.User')),
                ('planner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planned_weddings', to='home.User')),
            ],
        ),
    ]

# Generated by Django 2.2.24 on 2022-01-05 08:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('active', models.BooleanField()),
                ('title', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=256)),
                ('active', models.BooleanField(blank=True, null=True)),
                ('principal_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_principal_name', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

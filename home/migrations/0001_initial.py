# Generated by Django 4.0.4 on 2022-07-07 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SosUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('verified', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SosMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=1000)),
                ('number_of_people', models.IntegerField()),
                ('extra_message', models.TextField(max_length=1000)),
                ('medical_assistance', models.BooleanField()),
                ('sosuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.sosuser')),
            ],
        ),
    ]

# Generated by Django 3.2.4 on 2021-06-21 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='last name')),
                ('username', models.CharField(max_length=50, verbose_name='username')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Fmale')], default='F', max_length=1, verbose_name='gender')),
                ('phone_number', models.CharField(blank=True, max_length=11, verbose_name='phone number')),
                ('biography', models.CharField(max_length=50, null=True, verbose_name='biography')),
                ('country', models.CharField(max_length=20, null=True, verbose_name='country')),
                ('website', models.URLField(verbose_name='website')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='register date')),
                ('update_date', models.DateTimeField(verbose_name='update date')),
            ],
        ),
    ]

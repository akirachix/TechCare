# Generated by Django 3.2.7 on 2021-11-18 09:02

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=254)),
                ('region', models.CharField(max_length=50)),
                ('how_did_you_hear_about_us', models.CharField(choices=[('G', 'Google'), ('F', 'Facebook'), ('T', 'Twitter'), ('I', 'Instagram'), ('F', 'Friend')], default='Google', max_length=50)),
                ('message', models.TextField(max_length=250)),
            ],
        ),
    ]
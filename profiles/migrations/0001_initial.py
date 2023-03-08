# Generated by Django 3.2.18 on 2023-03-08 14:09

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('age_group', models.CharField(choices=[('Teenager (10 - 18)', 'Teenager'), ('Young Adult (19 - 25)', 'Young Adult'), ('Adult (26 - 40)', 'Adult'), ('Middle Aged (41 - 60)', 'Middle Aged'), ('Senior (>61)', 'Senior')], max_length=50)),
                ('brief_bio', models.TextField(blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(default='../default_profile_afxozd', upload_to='images/')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]

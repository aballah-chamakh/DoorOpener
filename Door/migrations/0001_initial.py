# Generated by Django 2.0 on 2019-07-09 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0002_remove_profile_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Door',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('opened', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='account.Profile')),
            ],
        ),
    ]
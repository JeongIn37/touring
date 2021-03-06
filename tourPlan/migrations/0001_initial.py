# Generated by Django 3.0 on 2020-08-29 18:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departDate', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('arriveDate', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('hotel', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='작성시간')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='수정시간')),
            ],
        ),
    ]

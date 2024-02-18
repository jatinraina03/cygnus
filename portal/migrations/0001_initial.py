# Generated by Django 4.2.5 on 2023-09-15 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_text', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=100, null=True)),
                ('pub_date', models.DateTimeField(verbose_name='Date Published')),
            ],
        ),
    ]
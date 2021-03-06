# Generated by Django 2.2.1 on 2021-07-06 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hod', '0002_stu_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='parents_feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=50)),
                ('par_relation', models.CharField(max_length=200)),
                ('par_name', models.CharField(max_length=50)),
                ('par_ph_no', models.CharField(max_length=10)),
                ('par_email', models.CharField(max_length=200)),
                ('par1', models.CharField(max_length=20)),
                ('par2', models.CharField(max_length=20)),
                ('par3', models.CharField(max_length=20)),
                ('par4', models.CharField(max_length=20)),
                ('par5', models.CharField(max_length=20)),
                ('par6', models.CharField(max_length=20)),
                ('par7', models.CharField(max_length=500)),
            ],
        ),
    ]

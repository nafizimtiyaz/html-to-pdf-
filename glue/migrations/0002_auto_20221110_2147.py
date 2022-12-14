# Generated by Django 3.1.4 on 2022-11-10 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glue', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new',
            old_name='present',
            new_name='present_address',
        ),
        migrations.AddField(
            model_name='new',
            name='h_s_p_year',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='new',
            name='h_school',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='new',
            name='hons_p_year',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='new',
            name='hons_school',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='new',
            name='permanent_address',
            field=models.TextField(blank=True, max_length=600),
        ),
        migrations.AddField(
            model_name='new',
            name='s_s_p_year',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='new',
            name='s_school',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='new',
            name='soft_skill',
            field=models.TextField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='new',
            name='work_desig_one',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='new',
            name='work_desig_three',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='new',
            name='work_desig_two',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='new',
            name='work_ex_c_name_one',
            field=models.TextField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='new',
            name='work_ex_c_name_three',
            field=models.TextField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='new',
            name='work_ex_c_name_two',
            field=models.TextField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='new',
            name='work_year_one',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='new',
            name='work_year_three',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='new',
            name='work_year_two',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]

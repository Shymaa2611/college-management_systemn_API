# Generated by Django 4.2.3 on 2023-07-14 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_department_department_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.CharField(choices=[('IS', 'IS'), ('BIO', 'BIO'), ('None', 'None'), ('CS', 'CS')], max_length=10, verbose_name='department'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_level',
            field=models.CharField(choices=[('2', '2'), ('4', '4'), ('3', '3'), ('1', '1')], max_length=1, verbose_name='level'),
        ),
        migrations.DeleteModel(
            name='Faculty',
        ),
    ]
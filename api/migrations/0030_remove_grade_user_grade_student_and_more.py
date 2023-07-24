# Generated by Django 4.2.3 on 2023-07-24 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_alter_student_department_alter_student_student_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='user',
        ),
        migrations.AddField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(choices=[('None', 'None'), ('BIO', 'BIO'), ('IS', 'IS'), ('CS', 'CS')], max_length=5),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_level',
            field=models.CharField(choices=[('2', '2'), ('1', '1'), ('4', '4'), ('3', '3')], max_length=1, verbose_name='level'),
        ),
    ]
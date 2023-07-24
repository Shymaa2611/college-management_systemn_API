# Generated by Django 4.2.3 on 2023-07-24 20:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0022_remove_student_student_courses_student_course_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='grade',
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(choices=[('None', 'None'), ('IS', 'IS'), ('BIO', 'BIO'), ('CS', 'CS')], max_length=5),
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.DecimalField(decimal_places=2, max_digits=11)),
                ('Course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.course')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
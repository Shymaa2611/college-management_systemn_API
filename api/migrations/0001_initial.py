# Generated by Django 4.2.3 on 2023-07-14 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(blank=True, max_length=20, null=True, verbose_name='course')),
                ('course_score', models.IntegerField(default=0, verbose_name='score')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(choices=[('IS', 'IS'), ('BIO', 'BIO'), ('None', 'None'), ('CS', 'CS')], max_length=10, verbose_name='department')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department', to='api.course')),
            ],
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_first_number', models.CharField(blank=True, max_length=11, null=True, verbose_name='First Number')),
                ('mobile_second_number', models.CharField(blank=True, max_length=11, null=True, verbose_name='Second Number')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15, verbose_name='first name')),
                ('last_name', models.CharField(max_length=15, verbose_name='last name')),
                ('student_age', models.IntegerField(default=0, verbose_name='age')),
                ('student_address', models.CharField(max_length=20, verbose_name='address')),
                ('student_GPA', models.DecimalField(decimal_places=2, max_digits=3)),
                ('student_level', models.CharField(choices=[('2', '2'), ('3', '3'), ('1', '1'), ('4', '4')], max_length=1, verbose_name='level')),
                ('cousre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.course')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student', to='api.department', verbose_name='department')),
                ('student_mobile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student', to='api.mobile')),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15, verbose_name='first name')),
                ('last_name', models.CharField(max_length=15, verbose_name='last name')),
                ('instructor_salary', models.DecimalField(decimal_places=2, max_digits=2, verbose_name='salary')),
                ('course', models.ManyToManyField(related_name='instructor', to='api.course')),
                ('mobile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instructor', to='api.mobile', verbose_name='mobile')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=20, verbose_name='faculty')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faculty', to='api.department')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department', to='api.instructor'),
        ),
    ]

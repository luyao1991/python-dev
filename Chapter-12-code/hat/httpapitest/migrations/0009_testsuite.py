# Generated by Django 2.2.2 on 2019-07-25 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('httpapitest', '0008_env'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestSuite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('suite_name', models.CharField(max_length=100)),
                ('include', models.TextField()),
                ('belong_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='httpapitest.Project')),
            ],
            options={
                'verbose_name': '用例集合',
                'db_table': 'TestSuite',
            },
        ),
    ]

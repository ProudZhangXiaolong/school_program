# Generated by Django 3.2.4 on 2021-06-21 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10, null=True, verbose_name='与老师对应的工号')),
                ('type', models.CharField(max_length=10, null=True, verbose_name='活动类型')),
                ('title', models.CharField(max_length=10, null=True, verbose_name='活动主题')),
                ('people', models.CharField(max_length=10, null=True, verbose_name='活动对象')),
                ('image', models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='上传照片')),
                ('content', models.TextField(blank=True, null=True, verbose_name='活动内容')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('link_teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.teacher', verbose_name='活动关联的老师')),
            ],
            options={
                'verbose_name': '三二一活动',
                'verbose_name_plural': '三二一活动',
            },
        ),
    ]
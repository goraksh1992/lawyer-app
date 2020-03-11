# Generated by Django 3.0.4 on 2020-03-10 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_lawyerfeedback'),
        ('blog', '0002_blogcommentmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogLikeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.CharField(default='1', max_length=2)),
                ('like_date', models.DateTimeField(auto_now_add=True)),
                ('blog_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.BlogModel')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserModel')),
            ],
        ),
    ]
# Generated by Django 3.0.4 on 2020-03-08 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lawyer_panel', '0002_lawyermodel_password'),
        ('user', '0006_auto_20200308_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentsmodel',
            name='lawyer_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lawyer_panel.LawyerModel'),
        ),
        migrations.AlterField(
            model_name='appointmentsmodel',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.UserModel'),
        ),
    ]

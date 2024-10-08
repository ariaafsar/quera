# Generated by Django 4.2.11 on 2024-10-09 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=100)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.account')),
                ('students', models.ManyToManyField(related_name='student', to='user.account')),
                ('teachers', models.ManyToManyField(related_name='teacher', to='user.account')),
            ],
        ),
    ]

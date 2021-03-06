# Generated by Django 2.2.6 on 2020-01-13 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoleMaster',
            fields=[
                ('role_id', models.BigAutoField(auto_created=True, db_column='role_id', primary_key=True, serialize=False)),
                ('role_name', models.CharField(db_column='role_name', max_length=100)),
                ('status', models.CharField(db_column='status', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='UserMaster',
            fields=[
                ('user_id', models.CharField(db_column='user_id', max_length=7, primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserRoleAssociation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, db_column='id', primary_key=True, serialize=False)),
                ('role_id', models.ForeignKey(db_column='role_id', on_delete=django.db.models.deletion.CASCADE, to='services.RoleMaster')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='services.UserMaster')),
            ],
        ),
    ]

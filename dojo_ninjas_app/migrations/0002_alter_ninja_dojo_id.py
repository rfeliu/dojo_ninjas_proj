# Generated by Django 4.1 on 2022-09-16 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ninja',
            name='dojo_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ninjas', to='dojo_ninjas_app.dojo'),
        ),
    ]

# Generated by Django 4.2.3 on 2023-12-29 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("prevalence", "0007_alter_patientsbysource_source"),
    ]

    operations = [
        migrations.AddField(
            model_name="diseasestats",
            name="global_stats",
            field=models.ForeignKey(
                default=12,
                on_delete=django.db.models.deletion.CASCADE,
                to="prevalence.globalstats",
            ),
            preserve_default=False,
        ),
    ]

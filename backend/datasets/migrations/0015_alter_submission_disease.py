# Generated by Django 4.2.3 on 2024-01-15 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("prevalence", "0009_alter_disease_do_id"),
        ("datasets", "0014_alter_submission_disease"),
    ]

    operations = [
        migrations.AlterField(
            model_name="submission",
            name="disease",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="prevalence.disease",
            ),
        ),
    ]
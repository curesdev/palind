# Generated by Django 4.2.3 on 2023-12-27 16:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("prevalence", "0002_urlsource_disease"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="diseasestats",
            options={
                "verbose_name": "  Disease Stats",
                "verbose_name_plural": "  Disease Stats",
            },
        ),
        migrations.AlterModelOptions(
            name="globalstats",
            options={
                "verbose_name": "   Global Stats",
                "verbose_name_plural": "   Global Stats",
            },
        ),
        migrations.AlterModelOptions(
            name="patientsbysource",
            options={
                "verbose_name": " Patients by Source",
                "verbose_name_plural": " Patients by Source",
            },
        ),
        migrations.AlterModelOptions(
            name="urlsource",
            options={"verbose_name": "URL Source"},
        ),
        migrations.AddField(
            model_name="disease",
            name="icd10_id",
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name="disease",
            name="omim_id",
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name="disease",
            name="orpha_id",
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name="disease",
            name="snomed_id",
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name="disease",
            name="synonyms",
            field=models.TextField(blank=True),
        ),
    ]

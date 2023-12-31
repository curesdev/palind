# Generated by Django 4.2.3 on 2023-12-07 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("prevalence", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="urlsource",
            name="disease",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="prevalence.disease",
            ),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.3 on 2023-11-28 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0009_customuser_default_dataset"),
        ("datasets", "0007_remove_submission_gender_token_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dataset",
            name="organization",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="accounts.organization",
            ),
        ),
    ]

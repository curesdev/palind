# Generated by Django 4.2.3 on 2023-11-02 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="organization",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="accounts.organization",
            ),
        ),
    ]

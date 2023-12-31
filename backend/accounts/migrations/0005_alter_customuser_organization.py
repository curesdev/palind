# Generated by Django 4.2.3 on 2023-11-02 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "accounts",
            "0004_alter_customuser_managers_remove_customuser_username_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="users",
                to="accounts.organization",
            ),
        ),
    ]

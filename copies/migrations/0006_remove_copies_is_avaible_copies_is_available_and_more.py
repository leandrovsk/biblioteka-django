# Generated by Django 4.2.1 on 2023-05-04 19:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("copies", "0005_alter_book_loans_finished_at_alter_book_loans_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="copies",
            name="is_avaible",
        ),
        migrations.AddField(
            model_name="copies",
            name="is_available",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="book_loans",
            name="finished_at",
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="book_loans",
            name="status",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="copies",
            name="last_loan",
            field=models.DateTimeField(null=True),
        ),
    ]

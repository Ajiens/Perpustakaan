from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Member",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "role",
                    models.CharField(
                        choices=[("customer", "Pelanggan"), ("employee", "Karyawan")],
                        max_length=10,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("member", "Member"), ("non_member", "Non-Member")],
                        max_length=10,
                    ),
                ),
            ],
        ),
    ]
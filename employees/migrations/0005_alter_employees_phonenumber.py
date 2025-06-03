from django.db import migrations, models
from django.db.migrations.operations.special import RunSQL

class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_alter_employees_email_alter_employees_phonenumber'),
    ]

    operations = [
        RunSQL("DROP VIEW IF EXISTS employee_with_department;"),

        migrations.AlterField(
            model_name='employees',
            name='phoneNumber',
            field=models.CharField(max_length=30),  # Or 40, depending on your faker
        ),

        RunSQL("""
        CREATE VIEW employee_with_department AS
        SELECT 
            e.id,
            e.name,
            e.email,
            e."phoneNumber",
            e.address,
            e."dateOfJoining",
            d.department AS department_name
        FROM employees_employees e
        JOIN employees_department d ON e.department_id = d.id;
        """),
    ]

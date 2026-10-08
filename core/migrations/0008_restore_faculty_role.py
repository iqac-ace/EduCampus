from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_progresssubmission_subtopic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(
                choices=[
                    ('IQAC', 'IQAC Coordinator'),
                    ('HOD', 'Head of Department'),
                    ('FACULTY', 'Faculty'),
                    ('STUDENT', 'Student'),
                ],
                max_length=10,
            ),
        ),
    ]

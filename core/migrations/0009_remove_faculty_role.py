from django.db import migrations, models


def convert_legacy_faculty_to_hod(apps, schema_editor):
    Profile = apps.get_model('core', 'Profile')
    Profile.objects.filter(role='FACULTY').update(role='HOD')


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_restore_faculty_role'),
    ]

    operations = [
        migrations.RunPython(
            convert_legacy_faculty_to_hod,
            migrations.RunPython.noop,
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(
                choices=[
                    ('IQAC', 'IQAC Coordinator'),
                    ('HOD', 'Head of Department'),
                    ('STUDENT', 'Student'),
                ],
                max_length=10,
            ),
        ),
    ]

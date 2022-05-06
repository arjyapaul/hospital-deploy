

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0021_auto_20220129_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pathologist',
            name='mobile',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pathologist',
            name='role',
            field=models.CharField(choices=[('full time pathologist', 'full time pathologist'), ('lab assistant', 'lab assistant'), ('lab technician', 'lab technician')], default='fulltime', max_length=50),
        ),
    ]

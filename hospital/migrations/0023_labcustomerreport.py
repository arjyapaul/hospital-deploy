

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0022_auto_20220129_2230'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabcustomerReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labcustomerId', models.PositiveIntegerField(null=True)),
                ('labcustomerName', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('test', models.CharField(max_length=100, null=True)),
                ('scheduledate', models.CharField(max_length=30)),
                ('testDetail', models.CharField(max_length=200)),
                ('testResult', models.CharField(max_length=200)),
                ('conclusion', models.CharField(max_length=200)),
                ('charge', models.PositiveIntegerField()),
            ],
        ),
    ]

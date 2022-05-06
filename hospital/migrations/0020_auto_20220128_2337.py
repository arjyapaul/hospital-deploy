

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0019_auto_20220122_0154'),
    ]

    operations = [
        migrations.AddField(
            model_name='labcustomer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/LabcustomerProfilePic/'),
        ),
        migrations.AlterField(
            model_name='labcustomer',
            name='mobile',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='labcustomer',
            name='test',
            field=models.CharField(choices=[('blood test', 'blood test'), ('sugar test', 'sugar test'), ('lipid profile', 'lipid profile'), ('liver function test', 'liver function test'), ('urine analysis', 'urine analysis'), ('kidney function test', 'kidney function test'), ('thyroid test', 'thyroid test')], default='blood test', max_length=40),
        ),
    ]

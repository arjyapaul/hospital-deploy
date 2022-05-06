

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0018_auto_20201015_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='reception',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/ReceptionProfilePic/'),
        ),
        migrations.AlterField(
            model_name='reception',
            name='mobile',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='reception',
            name='position',
            field=models.CharField(choices=[('fulltime', 'fulltime'), ('part-time', 'part-time')], default='fulltime', max_length=50),
        ),
    ]

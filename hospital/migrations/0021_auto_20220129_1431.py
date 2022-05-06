

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0020_auto_20220128_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='pathologist',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/PathologistProfilePic/'),
        ),
        migrations.AlterField(
            model_name='pathologist',
            name='mobile',
            field=models.CharField(max_length=20),
        ),
    ]

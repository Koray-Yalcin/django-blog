
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_poststatistic'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PostStatistic',
        ),
    ]

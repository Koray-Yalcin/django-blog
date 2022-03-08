
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]

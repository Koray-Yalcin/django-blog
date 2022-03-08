
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_remove_post_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]

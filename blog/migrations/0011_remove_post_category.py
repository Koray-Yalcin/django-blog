
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_post_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=130, null=True, unique=True),
        ),
    ]


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_auto_20210110_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True, unique=True),
        ),
    ]

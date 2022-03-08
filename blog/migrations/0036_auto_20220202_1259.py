
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0035_auto_20210110_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]

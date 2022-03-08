
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0034_auto_20210110_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(editable=False, null=True, unique=True),
        ),
    ]

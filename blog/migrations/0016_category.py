
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(default='', max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='category')),
            ],
        ),
    ]

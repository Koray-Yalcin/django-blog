
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Başlık')),
                ('content', models.TextField(verbose_name='İçerik')),
                ('publishing_date', models.DateTimeField(auto_now_add=True, verbose_name='Yayınlanma Tarihi')),
                ('image', models.ImageField(blank=True, null=True, upload_to='post')),
                ('slug', models.SlugField(editable=False, max_length=130, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-publishing_date', 'id'],
            },
        ),
    ]

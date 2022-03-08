
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210108_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('software', 'yazilim'), ('product', 'urun'), ('game', 'oyun'), ('book', 'kitap'), ('movie', 'film')], default='software', max_length=10),
        ),
    ]
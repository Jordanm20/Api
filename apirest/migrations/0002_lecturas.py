from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('apirest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.TextField()),
                ('value', models.FloatField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

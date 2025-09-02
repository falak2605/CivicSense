from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('road', 'Road'), ('garbage', 'Garbage'), ('water', 'Water'), ('electricity', 'Electricity'), ('other', 'Other')], default='other', max_length=50)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Resolved', 'Resolved')], default='Pending', max_length=20)),
                ('location_lat', models.FloatField(blank=True, null=True)),
                ('location_lng', models.FloatField(blank=True, null=True)),
                ('upvotes', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

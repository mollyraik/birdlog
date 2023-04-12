# Generated by Django 4.1.7 on 2023-04-12 15:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0004_nest'),
    ]

    operations = [
        migrations.AddField(
            model_name='bird',
            name='nest_materials',
            field=models.ManyToManyField(to='main_app.nest'),
        ),
        migrations.AddField(
            model_name='bird',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('type', models.CharField(choices=[('I', 'Insects'), ('S', 'Seeds'), ('B', 'Berries'), ('F', 'Fish'), ('R', 'Rodents')], default='I', max_length=1)),
                ('bird', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.bird')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]

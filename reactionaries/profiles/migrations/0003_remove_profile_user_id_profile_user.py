# Generated by Django 4.0.2 on 2023-04-04 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0002_initial'),
    ]

    # operations = [
    #     migrations.RemoveField(
    #         model_name='profile',
    #         name='user_id',
    #     ),
    #     migrations.AddField(
    #         model_name='profile',
    #         name='user',
    #         field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
    #         preserve_default=False,
    #     ),
    # ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_id',
            new_name='user'
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        )
    ]
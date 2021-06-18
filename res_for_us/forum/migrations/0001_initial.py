# Generated by Django 3.2.3 on 2021-06-18 03:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import forum.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=5000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=5000, null=True)),
                ('subject', models.CharField(max_length=255)),
                ('address', models.TextField(max_length=1000)),
                ('mainphoto', forum.fields.ThumbnailImageField(upload_to='')),
                ('cleaned', models.IntegerField()),
                ('taste', models.IntegerField()),
                ('kindness', models.IntegerField()),
                ('last_updated', models.DateField(auto_now_add=True, null=True)),
                ('slug', models.SlugField(allow_unicode=True, help_text='one word for title alias', max_length=100, verbose_name='SLUG')),
                ('writter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='forums', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'forum',
                'verbose_name_plural': 'forumss',
                'db_table': 'forum_forum',
                'ordering': ('-last_updated',),
            },
        ),
    ]

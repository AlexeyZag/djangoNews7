# Generated by Django 3.1.5 on 2021-01-20 22:15

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
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100, unique=True)),
                ('subscribers', models.ManyToManyField(blank=True, null=True, related_name='subscription', to=settings.AUTH_USER_MODEL, verbose_name='Подписчики')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_default_news', models.CharField(choices=[('Статья', 'Статья'), ('Новость', 'Новость')], default='Новость', max_length=7, verbose_name='Новость или статья')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('headline', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('text', models.TextField()),
                ('rating_of_post', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.author', verbose_name='Автор')),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.category')),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(related_name='categories', through='news.PostCategory', to='news.Category', verbose_name='Тэг'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('com_text', models.TextField()),
                ('com_time', models.DateTimeField(auto_now_add=True)),
                ('com_rating', models.IntegerField(default=0)),
                ('comment_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.post')),
                ('comment_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

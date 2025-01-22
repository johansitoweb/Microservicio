# Generated by Django 3.2.16 on 2023-05-02 21:19

import apps.posts.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('picture', models.ImageField(blank=True, default='media/users/user_default_profile.png', null=True, upload_to='media/users/pictures/', verbose_name='Picture')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('short_description', models.TextField(blank=True, max_length=125, null=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to=apps.posts.models.blog_directory_path)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField(default=uuid.uuid4, unique=True)),
                ('rating_number', models.IntegerField(blank=True, default=0, null=True)),
                ('language', models.CharField(blank=True, max_length=50, null=True)),
                ('level', models.CharField(blank=True, max_length=50, null=True)),
                ('views', models.IntegerField(blank=True, default=0)),
                ('clicks', models.IntegerField(blank=True, default=0, null=True)),
                ('impressions', models.IntegerField(blank=True, default=0, null=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.author')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='posts_category', to='category.category')),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='ViewCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=255)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_view_count', to='posts.post')),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('user', models.UUIDField(blank=True, null=True)),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rate_belongs_to_post', to='posts.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='rating',
            field=models.ManyToManyField(blank=True, related_name='courseRating', to='posts.Rate'),
        ),
        migrations.AddField(
            model_name='post',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sub_category_posts', to='category.category'),
        ),
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='topic_posts', to='category.category'),
        ),
    ]

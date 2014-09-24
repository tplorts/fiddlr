# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import fwa.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=62)),
                ('latitude', models.DecimalField(decimal_places=7, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=7, max_digits=10)),
            ],
            options={
            },
            bases=(models.Model, fwa.models.NamedModel),
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=126)),
                ('brief', models.CharField(blank=True, max_length=126)),
                ('lengthy', models.TextField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='')),
                ('isPublic', models.BooleanField(default=False)),
                ('website', models.URLField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('logo', models.ImageField(blank=True, upload_to='')),
                ('isOfficial', models.BooleanField(default=False)),
                ('area', models.ForeignKey(blank=True, related_name='artists', null=True, to='fwa.Area')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, fwa.models.NamedModel),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=62)),
            ],
            options={
            },
            bases=(models.Model, fwa.models.NamedModel),
        ),
        migrations.CreateModel(
            name='CreaCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=62)),
                ('roots', models.ManyToManyField(to='fwa.CreaCategory', blank=True, related_name='kin')),
            ],
            options={
            },
            bases=(models.Model, fwa.models.NamedModel),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=126)),
                ('brief', models.CharField(blank=True, max_length=126)),
                ('lengthy', models.TextField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='')),
                ('isPublic', models.BooleanField(default=False)),
                ('price', models.DecimalField(blank=True, decimal_places=4, null=True, max_digits=12)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('settimes', models.CharField(blank=True, max_length=200)),
                ('reserve', models.BooleanField(default=False)),
                ('ticket', models.BooleanField(default=False)),
                ('artist', models.ForeignKey(blank=True, related_name='events', null=True, to='fwa.Artist')),
                ('attendees', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True, related_name='attending')),
                ('coartists', models.ManyToManyField(to='fwa.Artist', blank=True, related_name='coevents')),
                ('editors', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True)),
                ('followers', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True, related_name='eventsFollowing')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, fwa.models.NamedModel),
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('image', models.ImageField(upload_to='')),
                ('caption', models.CharField(blank=True, max_length=126)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PictureAlbum',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=126)),
                ('about', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'picture alba',
            },
            bases=(models.Model, fwa.models.TitledModel),
        ),
        migrations.CreateModel(
            name='PictureAlbumEntry',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('ordinal', models.FloatField(blank=True, null=True)),
                ('album', models.ForeignKey(to='fwa.PictureAlbum')),
                ('picture', models.ForeignKey(to='fwa.Picture')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Placard',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=126)),
                ('body', models.TextField(blank=True)),
                ('active', models.BooleanField(default=True)),
                ('event', models.ForeignKey(blank=True, null=True, to='fwa.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlacardItem',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('text', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('pictureAlbum', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, null=True, to='fwa.PictureAlbum')),
                ('placard', models.ForeignKey(to='fwa.Placard', related_name='items')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=126)),
                ('brief', models.CharField(blank=True, max_length=126)),
                ('lengthy', models.TextField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='')),
                ('isPublic', models.BooleanField(default=False)),
                ('price', models.DecimalField(blank=True, decimal_places=4, null=True, max_digits=12)),
                ('artist', models.ForeignKey(blank=True, related_name='products', null=True, to='fwa.Artist')),
                ('coartists', models.ManyToManyField(to='fwa.Artist', blank=True, related_name='coproducts')),
                ('editors', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True)),
                ('followers', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True, related_name='productsFollowing')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, fwa.models.NamedModel),
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=126)),
                ('brief', models.CharField(blank=True, max_length=126)),
                ('lengthy', models.TextField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='')),
                ('isPublic', models.BooleanField(default=False)),
                ('website', models.URLField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('logo', models.ImageField(blank=True, upload_to='')),
                ('isOfficial', models.BooleanField(default=False)),
                ('address', models.CharField(blank=True, max_length=126)),
                ('categories', models.ManyToManyField(to='fwa.CreaCategory', blank=True, related_name='venues')),
                ('editors', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True)),
                ('followers', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True, related_name='venuesFollowing')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, fwa.models.NamedModel),
        ),
        migrations.AddField(
            model_name='placard',
            name='product',
            field=models.ForeignKey(blank=True, null=True, to='fwa.Product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='picturealbum',
            name='pictures',
            field=models.ManyToManyField(to='fwa.Picture', blank=True, through='fwa.PictureAlbumEntry'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(to='fwa.Venue', related_name='events'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='categories',
            field=models.ManyToManyField(to='fwa.CreaCategory', blank=True, related_name='artists'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='editors',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='followers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True, related_name='artistsFollowing'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='area',
            name='city',
            field=models.ForeignKey(to='fwa.City', related_name='areas'),
            preserve_default=True,
        ),
    ]

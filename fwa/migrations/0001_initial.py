# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(blank=True, max_length=200)),
                ('latitude', models.DecimalField(max_digits=10, decimal_places=7)),
                ('longitude', models.DecimalField(max_digits=10, decimal_places=7)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(blank=True, max_length=200)),
                ('brief', models.CharField(blank=True, max_length=200)),
                ('lengthy', models.TextField(blank=True)),
                ('picture', models.ImageField(upload_to='', blank=True)),
                ('public', models.BooleanField(default=False)),
                ('website', models.URLField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('logo', models.ImageField(upload_to='', blank=True)),
                ('official', models.BooleanField(default=False)),
                ('area', models.ForeignKey(related_name='artists', to='fwa.Area', null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CreaCategory',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(blank=True, max_length=200)),
                ('roots', models.ManyToManyField(to='fwa.CreaCategory', blank=True, related_name='kin')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(blank=True, max_length=200)),
                ('brief', models.CharField(blank=True, max_length=200)),
                ('lengthy', models.TextField(blank=True)),
                ('picture', models.ImageField(upload_to='', blank=True)),
                ('public', models.BooleanField(default=False)),
                ('price', models.DecimalField(null=True, max_digits=12, blank=True, decimal_places=4)),
                ('start', models.DateTimeField(null=True, blank=True)),
                ('end', models.DateTimeField(null=True, blank=True)),
                ('settimes', models.CharField(blank=True, max_length=200)),
                ('reserve', models.BooleanField(default=False)),
                ('ticket', models.BooleanField(default=False)),
                ('artist', models.ForeignKey(related_name='events', to='fwa.Artist', null=True, blank=True)),
                ('attendees', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True, related_name='attending')),
                ('coartists', models.ManyToManyField(to='fwa.Artist', blank=True, related_name='coevents')),
                ('editors', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True)),
                ('followers', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True, related_name='eventsFollowing')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to='')),
                ('caption', models.CharField(blank=True, max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PictureAlbum',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(blank=True, max_length=200)),
                ('about', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'picture alba',
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PictureAlbumEntry',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('ordinal', models.FloatField(null=True, blank=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(blank=True, max_length=200)),
                ('body', models.TextField(blank=True)),
                ('active', models.BooleanField(default=True)),
                ('event', models.ForeignKey(to='fwa.Event', null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlacardItem',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('text', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='', blank=True)),
                ('pictureAlbum', models.ForeignKey(to='fwa.PictureAlbum', null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True)),
                ('placard', models.ForeignKey(to='fwa.Placard', related_name='items')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(blank=True, max_length=200)),
                ('brief', models.CharField(blank=True, max_length=200)),
                ('lengthy', models.TextField(blank=True)),
                ('picture', models.ImageField(upload_to='', blank=True)),
                ('public', models.BooleanField(default=False)),
                ('price', models.DecimalField(null=True, max_digits=12, blank=True, decimal_places=4)),
                ('release', models.DateField(null=True, blank=True)),
                ('artist', models.ForeignKey(related_name='products', to='fwa.Artist', null=True, blank=True)),
                ('coartists', models.ManyToManyField(to='fwa.Artist', blank=True, related_name='coproducts')),
                ('editors', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True)),
                ('followers', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True, related_name='productsFollowing')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(blank=True, max_length=200)),
                ('brief', models.CharField(blank=True, max_length=200)),
                ('lengthy', models.TextField(blank=True)),
                ('picture', models.ImageField(upload_to='', blank=True)),
                ('public', models.BooleanField(default=False)),
                ('website', models.URLField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('logo', models.ImageField(upload_to='', blank=True)),
                ('official', models.BooleanField(default=False)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('categories', models.ManyToManyField(to='fwa.CreaCategory', blank=True, related_name='venues')),
                ('editors', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True)),
                ('followers', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True, related_name='venuesFollowing')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='placard',
            name='product',
            field=models.ForeignKey(to='fwa.Product', null=True, blank=True),
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

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import fwa.models
from django.conf import settings
import django_extensions.db.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Creaty',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', editable=False, blank=True, default=django.utils.timezone.now)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(verbose_name='modified', editable=False, blank=True, default=django.utils.timezone.now)),
                ('uuid', django_extensions.db.fields.PostgreSQLUUIDField(name='uuid', unique=True, blank=True, editable=False)),
                ('slug', django_extensions.db.fields.AutoSlugField(editable=False, blank=True, populate_from='title')),
                ('title', models.CharField(max_length=200)),
                ('brief', models.CharField(max_length=200, blank=True)),
                ('about', models.TextField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to=fwa.models.entityPicturePath)),
                ('public', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('phone', models.CharField(max_length=30, blank=True)),
                ('address', models.CharField(max_length=300, blank=True)),
                ('maxDistance', models.PositiveIntegerField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, upload_to='')),
                ('official', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'creaties',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CreatyClass',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=126)),
                ('specialty', models.CharField(max_length=126)),
                ('roots', models.ManyToManyField(related_name='heirs', to='fwa.CreatyClass', blank=True)),
                ('targetCreatyClasses', models.ManyToManyField(related_name='suitorCreatyClasses', to='fwa.CreatyClass', blank=True)),
            ],
            options={
                'verbose_name_plural': 'creaty classes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CreatyClassInterest',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('positive', models.BooleanField(default=True)),
                ('creaty', models.ForeignKey(to='fwa.Creaty')),
                ('creatyClass', models.ForeignKey(to='fwa.CreatyClass')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CreatyContactPoint',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('intent', models.CharField(max_length=126, blank=True)),
                ('name', models.CharField(max_length=126, blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('phone', models.CharField(max_length=30, blank=True)),
                ('postal', models.CharField(max_length=500, blank=True)),
                ('creaty', models.ForeignKey(to='fwa.Creaty', related_name='contactPoints')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CreatyNexum',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('info', models.BigIntegerField(blank=True, default=0)),
                ('source', models.ForeignKey(to='fwa.Creaty', related_name='+')),
                ('target', models.ForeignKey(to='fwa.Creaty', related_name='+')),
            ],
            options={
                'verbose_name_plural': 'creaty nexa',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('caption', models.CharField(max_length=126, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PictureAlbum',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=126, blank=True)),
                ('about', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'picture alba',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PictureAlbumEntry',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('ordinal', models.FloatField(blank=True, null=True)),
                ('album', models.ForeignKey(to='fwa.PictureAlbum')),
                ('picture', models.ForeignKey(to='fwa.Picture')),
            ],
            options={
                'verbose_name_plural': 'picture album entries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Placard',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=126)),
                ('body', models.TextField(blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlacardItem',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('pictureAlbum', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='fwa.PictureAlbum', null=True)),
                ('placard', models.ForeignKey(to='fwa.Placard', related_name='items')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProgramItem',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('piece', models.CharField(max_length=126)),
                ('moreInfo', models.CharField(max_length=126, blank=True)),
                ('composer', models.CharField(max_length=126, blank=True)),
                ('ordinal', models.FloatField(blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', editable=False, blank=True, default=django.utils.timezone.now)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(verbose_name='modified', editable=False, blank=True, default=django.utils.timezone.now)),
                ('uuid', django_extensions.db.fields.PostgreSQLUUIDField(name='uuid', unique=True, blank=True, editable=False)),
                ('slug', django_extensions.db.fields.AutoSlugField(editable=False, blank=True, populate_from='title')),
                ('title', models.CharField(max_length=200)),
                ('brief', models.CharField(max_length=200, blank=True)),
                ('about', models.TextField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to=fwa.models.entityPicturePath)),
                ('public', models.BooleanField(default=False)),
                ('release', models.DateTimeField(blank=True, null=True)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
                'ordering': [],
                'get_latest_by': 'modified',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectClass',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=126)),
                ('roots', models.ManyToManyField(related_name='heirs', to='fwa.ProjectClass', blank=True)),
                ('typicalCreatyClasses', models.ManyToManyField(related_name='typicalProjectClasses', to='fwa.CreatyClass', blank=True)),
            ],
            options={
                'verbose_name_plural': 'project classes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectClassInterest',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('positive', models.BooleanField(default=True)),
                ('creaty', models.ForeignKey(to='fwa.Creaty')),
                ('projectClass', models.ForeignKey(to='fwa.ProjectClass')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectConsumption',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('info', models.BigIntegerField(blank=True, default=0)),
                ('project', models.ForeignKey(to='fwa.Project')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectCreaty',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('role', models.BigIntegerField(blank=True, default=0)),
                ('creaty', models.ForeignKey(to='fwa.Creaty')),
                ('project', models.ForeignKey(to='fwa.Project')),
            ],
            options={
                'verbose_name_plural': 'project creaties',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectPrice',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(max_digits=16, decimal_places=4)),
                ('category', models.CharField(max_length=126)),
                ('project', models.ForeignKey(to='fwa.Project', related_name='prices')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectTemporalInterval',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('label', models.CharField(max_length=200, blank=True)),
                ('project', models.ForeignKey(to='fwa.Project', related_name='intervals')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='project',
            name='consumers',
            field=models.ManyToManyField(related_name='consuming', through='fwa.ProjectConsumption', to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='creaties',
            field=models.ManyToManyField(related_name='projects', through='fwa.ProjectCreaty', to='fwa.Creaty', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='editors',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='fans',
            field=models.ManyToManyField(related_name='projectFaves', to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='programitem',
            name='interval',
            field=models.ForeignKey(to='fwa.ProjectTemporalInterval', related_name='programItems'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='placard',
            name='project',
            field=models.ForeignKey(blank=True, to='fwa.Project', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='picturealbum',
            name='pictures',
            field=models.ManyToManyField(through='fwa.PictureAlbumEntry', to='fwa.Picture', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creaty',
            name='classes',
            field=models.ManyToManyField(related_name='creaties', to='fwa.CreatyClass', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creaty',
            name='creatyClassInterests',
            field=models.ManyToManyField(related_name='interestedCreaties', through='fwa.CreatyClassInterest', to='fwa.CreatyClass', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creaty',
            name='editors',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creaty',
            name='enexa',
            field=models.ManyToManyField(related_name='inexa', through='fwa.CreatyNexum', to='fwa.Creaty', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creaty',
            name='fans',
            field=models.ManyToManyField(related_name='creatyFaves', to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creaty',
            name='projectClassInterests',
            field=models.ManyToManyField(related_name='interestedCreaties', through='fwa.ProjectClassInterest', to='fwa.ProjectClass', blank=True),
            preserve_default=True,
        ),
    ]

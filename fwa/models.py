from django.db import models
from django.contrib.auth.models import User


class TitledModel(models.Model):
    title = models.CharField(max_length=200, blank=True)

    def __str__(self):
        if len(self.title) > 0:
            return self.title
        return '(~untitled~)'

    class Meta:
        abstract = True

########################################################################

class EntityBase(TitledModel):
    brief = models.CharField(max_length=200, blank=True)
    lengthy = models.TextField(blank=True)
    picture = models.ImageField(blank=True)
    public = models.BooleanField(default=False)
    editors = models.ManyToManyField(User, blank=True)
    followers = models.ManyToManyField(
        User, related_name='%(class)ssFollowing', blank=True
    )

    class Meta(TitledModel.Meta):
        abstract = True

########################################################################

class CreaCategory(TitledModel):
    roots = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='kin',
        blank=True
    )

########################################################################

class CreaBase(EntityBase):
    website = models.URLField(blank=True)
    email = models.EmailField(max_length=254, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    logo = models.ImageField(blank=True)
    official = models.BooleanField(default=False)
    categories = models.ManyToManyField(
        CreaCategory, related_name='%(class)ss', blank=True
    )

    class Meta(EntityBase.Meta):
        abstract = True

########################################################################

class Venue(CreaBase):
    address = models.CharField(max_length=200, blank=True)
    # events from fk

########################################################################

class City(TitledModel):
    pass

class Area(TitledModel):
    city = models.ForeignKey(City, related_name='areas')
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)

########################################################################

class Artist(CreaBase):
    area = models.ForeignKey(
        Area, related_name='artists',
        null=True, blank=True
    )
    # events & products from fk
    # coevents & coproducts from m2m

########################################################################

class ProjectBase(EntityBase):
    artist = models.ForeignKey(
        Artist, related_name='%(class)ss', null=True, blank=True
    )
    coartists = models.ManyToManyField(
        Artist, related_name='co%(class)ss', blank=True
    )
    price = models.DecimalField(
        max_digits=12, decimal_places=4,
        null=True, blank=True
    )

    class Meta(EntityBase.Meta):
        abstract = True

########################################################################

class Event(ProjectBase):
    venue = models.ForeignKey(Venue, related_name='events')
    attendees = models.ManyToManyField(
        User, related_name='attending', blank=True
    )
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    settimes = models.CharField(max_length=200, blank=True)
    reserve = models.BooleanField(default=False)
    ticket = models.BooleanField(default=False)

########################################################################

class Product(ProjectBase):
    release = models.DateField(null=True, blank=True)

########################################################################

class Picture(models.Model):
    image = models.ImageField()
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        if len(self.caption) > 0:
            return self.caption
        return self.image

class PictureAlbum(TitledModel):
    about = models.TextField(blank=True)
    pictures = models.ManyToManyField(
        Picture, through='PictureAlbumEntry', blank=True
    )

    class Meta(TitledModel.Meta):
        verbose_name_plural = 'picture alba'

class PictureAlbumEntry(models.Model):
    picture = models.ForeignKey(Picture)
    album = models.ForeignKey(PictureAlbum)
    ordinal = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.picture) + '/' + str(self.album)

########################################################################

class Placard(TitledModel):
    body = models.TextField(blank=True)
    product = models.ForeignKey(Product, null=True, blank=True)
    event = models.ForeignKey(Event, null=True, blank=True)
    # items from fk
    active = models.BooleanField(default=True)

    def __str__(self):
        if len(self.title) > 0:
            return self.title
        if self.product:
            return str(self.product)
        if self.event:
            return str(self.event)
        return "It's a Mystery"

class PlacardItem(models.Model):
    placard = models.ForeignKey(Placard, related_name='items')
    text = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    pictureAlbum = models.ForeignKey(
        PictureAlbum, null=True, blank=True, on_delete=models.SET_NULL
    )


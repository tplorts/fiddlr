from django.db import models
from django.contrib.auth.models import User

from fwa.miscellany import strIs

########################################################################


class EntityBase(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(max_length=200)
    brief = models.CharField(max_length=200, blank=True)
    about = models.TextField(blank=True)
    website = models.URLField(blank=True)

    # Image to be displayed in place of the Lady
    picture = models.ImageField(blank=True)

    # Whether this profile can be viewed by anyone but its editors
    public = models.BooleanField(default=False)

    # Users who manage this entity's profile (i.e. can edit it)
    editors = models.ManyToManyField(User, blank=True)

    # Users who get updates about this entity
    fans = models.ManyToManyField(
        User, related_name='%(class)sFaves', blank=True
    )

    def __str__(self):
        return self.title


########################################################################


class EntityClass(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=126)

    # roots are the superclasses; heirs are the subclasses.
    roots = models.ManyToManyField(
        'self', related_name='heirs',
        symmetrical=False, blank=True
    )

    def __str__(self):
        return self.name


########################################################################


# class City(TitledModel):
#     pass

# class Area(TitledModel):
#     city = models.ForeignKey(City, related_name='areas')
#     latitude = models.DecimalField(max_digits=10, decimal_places=7)
#     longitude = models.DecimalField(max_digits=10, decimal_places=7)

# TODO: find a premade model of locations
# and then put that into the creaty model




class CreatyClass(EntityClass):
    class Meta:
        verbose_name_plural = 'creaty classes'

    # e.g. drawing (as opposed to the inherited field, name, e.g.
    # draftsman)
    specialty = models.CharField(max_length=126)

    # Creaty classes to which this class of creaty might connect.
    # The suitor classes are thus those types of creaties interested in
    # connecting with this type of creaty.
    targetCreatyClasses = models.ManyToManyField(
        'self', symmetrical=False, blank=True,
        related_name='suitorCreatyClasses',
    )

    # The kinds of projects which typically involve this class of creaty
    # typicalProjectClasses from m2m in ProjectClass


########################################################################


class Creaty(EntityBase):
    class Meta:
        verbose_name_plural = 'creaties'

    email = models.EmailField(max_length=254, blank=True)
    phone = models.CharField(max_length=30, blank=True)

    # contactPoints from fk in CreatyContactPoint

    # TODO: There will also be a broader-scale location field
    # for people who want to give a location without too much detail.
    address = models.CharField(max_length=300, blank=True)

    # How far this creaty is willing to travel for jobs
    # null => open to anything
    # units: kilometres
    maxDistance = models.PositiveIntegerField(null=True, blank=True)

    # Whereas the picture (defined above) is the main image to appear
    # on the profile page, the logo gives creaties the option to
    # specify a smaller image to be used in compact lists and such.
    logo = models.ImageField(blank=True)

    # Whether the profile is managed by the represented creaty. There
    # can be profiles for creaties which someone unassociated with that
    # creaty has made and filled out.
    official = models.BooleanField(default=False)

    # What sort of creaty this one considers itself.  We allow them
    # to choose any number of classes to which they think they belong.
    classes = models.ManyToManyField(
        CreatyClass, related_name='creaties', blank=True
    )

    # A nexum is a generic connection between creaties.
    # enexa are outgoing nexa, whereas inexa are incoming.
    # Outgoing means that this creaty initiated the connection;
    # and incoming means that another creaty initiated the connection
    # and it is directed at this creaty.
    enexa = models.ManyToManyField(
        'self', blank=True, symmetrical=False, related_name='inexa',
        through='CreatyNexum', through_fields=('source', 'target'),
    )

    # Types of creaties in which this particular creaty is interested.
    # This set of creaty classes overrides the set of creaty classes
    # specified in this creaty's class.
    creatyClassInterests = models.ManyToManyField(
        'CreatyClass', blank=True,
        related_name='interestedCreaties',
        through='CreatyClassInterest'
    )

    # Types of projects in which this particular creaty has an
    # interest, in addition to any specified in this creaty's classes.
    # This relation also carries any project classes which do not
    # interest this creaty.  Regardless of whether the interest entry
    # is positive or negative, it takes precedence over the typical
    # interests specified in this creaty's class.
    projectClassInterests = models.ManyToManyField(
        'ProjectClass', blank=True,
        related_name='interestedCreaties',
        through='ProjectClassInterest',
    )


class CreatyContactPoint(models.Model):
    creaty = models.ForeignKey(Creaty, related_name='contactPoints')

    # What to use this contact point for
    # e.g. 'Booking', 'Inquiries', 'Lessons', etc.
    intent = models.CharField(max_length=126, blank=True)

    # The name of the person/organization for this contact info, if
    # not the creaty itself. e.g. 'JA Broder Management'
    name = models.CharField(max_length=126, blank=True)

    email = models.EmailField(max_length=254, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    postal = models.CharField(max_length=500, blank=True)


class ProjectClassInterest(models.Model):
    creaty = models.ForeignKey(Creaty)
    projectClass = models.ForeignKey('ProjectClass')

    # Whether the creaty is interested in the class of project.
    # A negative entry means that the creaty has specified that it is
    # not interested in taking on this kind of project.
    positive = models.BooleanField(default=True)


class CreatyClassInterest(models.Model):
    creaty = models.ForeignKey(Creaty)
    creatyClass = models.ForeignKey(CreatyClass)

    # See explanation of positive above, in ProjectClassInterest
    positive = models.BooleanField(default=True)


########################################################################


class CreatyNexum(models.Model):
    class Meta:
        verbose_name_plural = 'creaty nexa'

    # The creaty which initiated this nexum
    source = models.ForeignKey(Creaty, related_name='+')

    # The creaty to which this nexum is directed
    target = models.ForeignKey(Creaty, related_name='+')

    # Determines the type of nexum.  To be used in a generic manner,
    # where each type of creaty has its own way of using this info.
    info = models.BigIntegerField(default=0, blank=True)

    def __str__(self):
        return '{}--{}->{}'.format(self.source, self.info, self.target)


########################################################################


class ProjectClass(EntityClass):
    class Meta:
        verbose_name_plural = 'project classes'

    # The kinds of creaties which tend to endeavor in this kind of
    # project.
    typicalCreatyClasses = models.ManyToManyField(
        CreatyClass, blank=True,
        related_name='typicalProjectClasses'
    )

    # interestedCreaties from m2m in Creaty


########################################################################


class Project(EntityBase):

    # Creaties which are either involved in any capacity, or just
    # generally connected to this project.  The nature of the
    # involvement/connection can be expressed in the 'info' field
    # in the ProjectCreaty model.
    creaties = models.ManyToManyField(
        Creaty, through='ProjectCreaty',
        blank=True, related_name='projects',
    )

    # e.g. people who buy an album, or attend a show.
    # Again, the 'info' field in the joining model, ProjectConsumption,
    # defines how the user is consuming this.
    consumers = models.ManyToManyField(
        User, through='ProjectConsumption',
        related_name='consuming', blank=True
    )

    release = models.DateTimeField(null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)

    # intervals from fk in ProjectTemporalInterval
    # prices from fk in ProjectPrice


class ProjectPrice(models.Model):
    project = models.ForeignKey(Project, related_name='prices')
    price = models.DecimalField(
        max_digits=16, decimal_places=4,
    )
    # e.g. 'student', 'senior', etc.
    category = models.CharField(max_length=126)

    def __str__(self):
        return '{}: ${} ({})'.format(
            self.category, self.price, self.project
        )


class ProjectTemporalInterval(models.Model):
    """
    This can be used to specify set times or, for example, two halves
    of a program with an intermission in between.
    """
    project = models.ForeignKey(Project, related_name='intervals')
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    label = models.CharField(max_length=200, blank=True)
    # programItems from fk in ProgramItem


class ProjectCreaty(models.Model):
    """The 'through' model for creaties' involvement in projects"""
    class Meta:
        verbose_name_plural = 'project creaties'
    project = models.ForeignKey(Project)
    creaty = models.ForeignKey(Creaty)
    role = models.BigIntegerField(default=0, blank=True)


class ProjectConsumption(models.Model):
    project = models.ForeignKey(Project)
    user = models.ForeignKey(User)
    info = models.BigIntegerField(default=0, blank=True)

    def __str__(self):
        return '{}--{}->{}'.format(self.user, self.info, self.project)


class ProgramItem(models.Model):
    interval = models.ForeignKey(
        ProjectTemporalInterval, related_name='programItems'
    )

    # The main label of the item
    piece = models.CharField(max_length=126)

    # Any more text to be placed within this entry, for example,
    # movements or instrumentation
    moreInfo = models.CharField(max_length=126, blank=True)

    composer = models.CharField(max_length=126, blank=True)
    ordinal = models.FloatField(null=True, blank=True)

    def __str__(self):
        # pylint: disable=no-member
        return '{} / {}'.format(self.interval.project, self.piece)


########################################################################


class Picture(models.Model):
    image = models.ImageField()
    caption = models.CharField(max_length=126, blank=True)

    def __str__(self):
        if len(self.caption) > 0:
            return self.caption
        return self.image


class PictureAlbum(models.Model):
    class Meta:
        verbose_name_plural = 'picture alba'
    name = models.CharField(max_length=126, blank=True)
    about = models.TextField(blank=True)
    pictures = models.ManyToManyField(
        Picture, through='PictureAlbumEntry', blank=True
    )

    def __str__(self):
        return self.name


class PictureAlbumEntry(models.Model):
    class Meta:
        verbose_name_plural = 'picture album entries'
    picture = models.ForeignKey(Picture)
    album = models.ForeignKey(PictureAlbum)
    ordinal = models.FloatField(null=True, blank=True)

    def __str__(self):
        return '{} / {}'.format(self.album, self.picture)


########################################################################


class Placard(models.Model):
    title = models.CharField(max_length=126)
    body = models.TextField(blank=True)
    project = models.ForeignKey(Project, null=True, blank=True)
    # items from fk
    active = models.BooleanField(default=True)

    def __str__(self):
        if len(self.title) > 0:
            return self.title
        if self.project:
            return str(self.project)
        return "It's a Mystery"


class PlacardItem(models.Model):
    placard = models.ForeignKey(Placard, related_name='items')
    text = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    pictureAlbum = models.ForeignKey(
        PictureAlbum, null=True, blank=True, on_delete=models.SET_NULL
    )



from django.db import models
from django.utils import timezone
from users.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify # new
from django.utils.translation import ugettext_lazy as _

ACTIVE = 1
DEACTIVATED  = 0

STATUSES = ((ACTIVE, _('Active')), (DEACTIVATED , _('Inactive')))


class Settings(models.Model):
    name = models.CharField(_('Costumer Name'), max_length=100, unique=True)
    slug = models.SlugField(unique=True, null=False, editable=False)
    address = models.CharField(_('Address'), blank=True, max_length=255)
    cell = models.CharField(_('Cell'), blank=True, max_length=255)
    cell_2 = models.CharField(_('Cell 2'), blank=True, max_length=255)
    phone = models.CharField(_('Telephone'), blank=True, max_length=255)
    fax = models.CharField(_('Fax'), blank=True, max_length=255)
    email = models.EmailField(_('Email'))
    website = models.CharField(_('Web Site'), max_length=255, blank=True)
    logo = models.ImageField(_('Logo'), max_length=255, blank=True)
    logo_square = models.ImageField(_('Logo Square'), max_length=255, blank=True)
    active_status = models.IntegerField(_('Status'), choices=STATUSES, default=ACTIVE)
    notes = models.TextField(blank=True)
    date_created = models.DateTimeField(editable=False, default=timezone.now)
    date_modified = models.DateTimeField(editable=False, default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="+")
    modified_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="+")

    def get_absolute_url(self):
        return reverse('maintenance_details', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Settings"
        verbose_name_plural = "Settings"
        ordering = ("name",)
    
    def __str__(self):
        return self.name


# -*- coding: utf-8 -*-
import random
import string

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

BASE = string.digits + string.ascii_letters
get_random_id = lambda: ''.join([random.choice(BASE) for i in range(12)])


class PublicIdModel(models.Model):
    """
    Abstract model that defines the 'public_id' field which is auto populated
    by a ramdom combination of 12 items iside the digits, lowercase and
    upercase letters.
    """
    public_id = models.CharField(
        unique=True,
        db_index=True,
        editable=False,
        max_length=12,
        verbose_name=_('public_id')
    )

    class Meta:
        abstract = True


@receiver(pre_save)
def populate_public_id(sender, instance, **kwargs):
    if issubclass(sender, PublicIdModel):
        while not instance.public_id:
            candidate = get_random_id()

            try:
                sender.objects.get(public_id=candidate)

            except sender.DoesNotExist:
                instance.public_id = candidate

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from core.models import TimeStampedModel


class Vote(TimeStampedModel):
    """Vote model."""

    value = models.IntegerField()
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.DO_NOTHING,
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(
        'content_type',
        'object_id'
    )

    @classmethod
    def create(cls, value, content_object):

        new_vote = cls(
            content_object=content_object,
            value=value
        )
        new_vote.save()
        return new_vote

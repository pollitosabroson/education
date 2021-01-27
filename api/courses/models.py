import logging

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import PublicIdModel, TimeStampedModel, VoteModel
from professors.models import Professor
from voting.models import Vote

logger = logging.getLogger(__name__)


class Course(
    PublicIdModel, TimeStampedModel, VoteModel, AbstractBaseUser
):

    USERNAME_FIELD = 'name'

    name = models.TextField(
        _('name'),
        help_text=_('name for course'),
        null=False, blank=False,
        unique=True,
    )

    professor = models.ForeignKey(
        Professor,
        on_delete=models.DO_NOTHING,
        related_name='courses'
    )

    vote = GenericRelation(Vote)

    class Meta:
        """
        Add verbose name
        """
        verbose_name = _('course')
        verbose_name_plural = _('courses')

    @classmethod
    def new_course(cls, name, professor):
        """.
        Args:
            name(str): Name of course
            professor(instance): Instance of professor
        Return:
            Instance: New instance of course
        """
        new_course = cls(
            name=name,
            professor=professor
        )
        new_course.save()
        return new_course

    def to_public_representation(self):
        """Dictionary with the public representation of the course.
        Return:
            Dict: Public representation
        """
        return {
            "id": self.public_id,
            "name": self.name,
            "professor": self.professor.to_public_representation(),
            "votes": self.vote_representation()
        }

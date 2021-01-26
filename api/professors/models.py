from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import PublicIdModel, TimeStampedModel


class Professor(
    PublicIdModel, TimeStampedModel, AbstractBaseUser
):
    USERNAME_FIELD = 'email'

    name = models.TextField(
        _('name'),
        help_text=_('name for professor'),
        null=True, blank=True
    )
    email = models.EmailField(
        _('email address'),
        blank=True,
        unique=True,
        help_text=_('I stand out in that an e-mail is stored')
    )

    class Meta:
        """
        Add verbose name
        """

        verbose_name = _('Professor')
        verbose_name_plural = _('Professors')

    def to_public_representation(self):
        """Create a public representation of the teacher.
        Return:
            Dict: Public representation
        """
        return {
            "id": self.public_id,
            "name": self.name,
            "email": self.email
        }

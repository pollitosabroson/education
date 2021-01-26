from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import PublicIdModel, TimeStampedModel


class Professor(
    PublicIdModel, TimeStampedModel, AbstractBaseUser
):

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

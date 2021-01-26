# -*- coding: utf-8 -*-
import logging

from django.db import models
from django.db.models import Count, Sum

logger = logging.getLogger(__name__)


class VoteModel(models.Model):
    """
    Abstract model where the values ​​based on the votes are obtained and calculated
    This model must be used as the base for all the models in the project.
    """  # NOQA

    class Meta:
        """
        Defination abstract Model
        """

        abstract = True

    def get_total_votes(self):
        """Get total votes.
        Return:
            Int: total of votes
        """
        return self.vote.count()

    def get_average_votes(self):
        """Calculate the total the average of the votes.
        Return:
            Int: Average votes
        """
        sum_votes = self.vote.aggregate(
            sum_values=Sum('value'), total_values=Count('value')
        )
        if sum_votes.get('total_values') > 0:
            return round(
                sum_votes.get(
                    'sum_values'
                ) / sum_votes.get('total_values'), 1
            )
        return 0

    def vote_representation(self):
        """Get representation for vote."""
        return {
            "total": self.get_total_votes(),
            "average": self.get_average_votes()
        }

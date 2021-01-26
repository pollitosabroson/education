import logging

from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from professors.models import Professor

from .models import Course

logger = logging.getLogger(__name__)


class CourseSerializer(serializers.ModelSerializer):
    """Professor Serializer."""

    professor_id = serializers.CharField(
        source="professor.public_id"
    )

    name = serializers.CharField(
        required=True
    )

    class Meta:
        """Meta class for professor Serializer."""
        model = Course
        fields = ('name', 'professor_id')

    def validate_name(self, value):
        """Check exists professor."""
        if Course.objects.filter(name=value).exists():
            raise serializers.ValidationError(
                _('There is already a course with this name')
            )
        return value

    def validate_professor_id(self, value):
        """Check exists professor.
        Args:
            Value(str): Public id of users
        Return:
            Instance: Instance of professor
        Raise:
            Raise: Error if there is no professor
        """
        professor = Professor.objects.filter(public_id=value)
        if not professor.exists():
            raise serializers.ValidationError(
                _('There is no professor')
            )
        else:
            return professor.first()

    def to_representation(self, instance):
        """Create a public representation of the course.
        Args:
            Instance(Instance): Instance of courser
        Return:
            Dict: Dicrt
        """
        return instance.to_public_representation()

    def create(self, validate_data):
        """Create new course.
        Args:
        validate_data(instance): Instance with all the data of the
        serializers and values ​​of the view
        Return:
            Instance: New course.
        """
        new_course = Course.new_course(
            name=validate_data.get('name'),
            professor=validate_data.get(
                'professor', {}
            ).get('public_id'),
        )
        return new_course

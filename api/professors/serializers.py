from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from .models import Professor


class ProfessorSerializer(serializers.ModelSerializer):
    """Professor Serializer."""

    id = serializers.CharField(
        read_only=True,
        source="public_id"
    )
    name = serializers.CharField(
        required=True
    )
    email = serializers.EmailField(
        required=True
    )

    class Meta:
        """Meta class for professor Serializer."""
        model = Professor
        fields = ('name', 'email', 'id')

    def validate_email(self, value):
        """Check exists professor."""
        if Professor.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                _('There is already a teacher with this email')
            )
        return value

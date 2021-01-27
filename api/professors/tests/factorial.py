import logging

from professors.models import Professor

logger = logging.getLogger(__name__)


class ProfessorFactory:
    """Class in charge of creating Professor objects"""

    @staticmethod
    def get_professor(name='Fake name', email='fake@email.com'):
        """Returns a professor with the received parameters.
        Args:
            name(str, Optional): Name of user
            email(str, Optional): Email of user
        Return:
            Instance: User Instance
        """
        if Professor.objects.filter(email=email).exists():
            return Professor.objects.get(email=email)
        data = {
            'name': name,
            'email': email
        }
        professor = Professor(**data)
        professor.save()
        return professor

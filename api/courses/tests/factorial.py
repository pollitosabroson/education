import logging

from courses.models import Course

logger = logging.getLogger(__name__)


class CourseFactory:
    """Class in charge of creating course objects"""

    @staticmethod
    def get_course(professor, name='Fake name'):
        """Returns a course with the received parameters.
        Args:
            name(str, Optional): Name of course
            professor(Instance): Instance of professor
        Return:
            Instance: User Instance
        """
        if Course.objects.filter(name=name).exists():
            return Course.objects.get(name=name)
        data = {
            'name': name,
            'professor': professor
        }
        course = Course(**data)
        course.save()
        return course

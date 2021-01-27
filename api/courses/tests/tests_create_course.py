import json
import logging

import pytest
from django.urls import reverse
from rest_framework import status

from core.utils import parse_response_content
from courses.schemas import conf_schema_course
from professors.tests.factorial import ProfessorFactory

from .factorial import CourseFactory

logger = logging.getLogger(__name__)


@pytest.mark.django_db
@pytest.mark.urls('education.urls')
class TestCreateCourses:
    """Specific tests for creating a Course."""

    url = reverse('courses:list_create_courses')
    @staticmethod
    def get_success_fixtures():
        """Course list for cases where the endpoint
        have an answer success
        """

        professor = ProfessorFactory.get_professor()
        return [
            {
                "name": "Create your own website for FREE!",
                "professor_id": professor.public_id,
            },
            {
                "name": "Disruptor Training",
                "professor_id": professor.public_id,
            },
            {
                "name": "Excel and Elevate Training",
                "professor_id": professor.public_id,
            }
        ]

    @staticmethod
    def get_bad_request_fixtures():
        """Course list for cases where the endpoint
        have a fail answer
        """
        name_course = "Excel and Elevate Training"
        professor = ProfessorFactory.get_professor()
        CourseFactory.get_course(
            professor=professor,
            name=name_course
        )
        return [
            {},
            {
                "name": name_course,
                "professor_id": professor.public_id,
            },
            {
                "name": "fake name test",
                "professor_id": "fake_id"
            }
        ]

    def make_post_request(self, client, params=None, **kwargs):
        """
        Make the request to the endpoint and return the content and status
        """
        headers = {
            'content_type': 'application/json'
        }
        i_params = params or {}
        body = {}
        body.update(**i_params)
        body = json.dumps(body)
        response = client.post(
            self.url,
            body,
            **headers
        )
        content = parse_response_content(response)
        status = response.status_code
        return content, status

    def test_success(self, client):
        """Test to validate that a Course will be edited with the
        parameters."""
        for fixtures in self.get_success_fixtures():
            response_content, response_status = self.make_post_request(
                client,
                params=fixtures
            )
            assert status.HTTP_201_CREATED == response_status
            assert conf_schema_course.is_valid(response_content)

    def test_bad_request(self, client):
        """Test to validate that a Course cannot be edited."""
        for fixtures in self.get_bad_request_fixtures():
            response_content, response_status = self.make_post_request(
                client,
                params=fixtures
            )
            assert status.HTTP_400_BAD_REQUEST == response_status

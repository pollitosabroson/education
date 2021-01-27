from schema import Or, Schema

from professors.schemas import conf_schema_professor
from voting.schemas.schema_vote import conf_schema_vote

conf_schema_course = Schema(
    {
        "id": str,
        "name": str,
        "professor": conf_schema_professor,
        "votes": conf_schema_vote
    }
)

conf_schema_list_courses = Schema(
    {
        "count": int,
        "next": Or(None, str),
        "previous": Or(None, str),
        "results": [
            conf_schema_course
        ]
    }
)

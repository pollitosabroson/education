from schema import Or, Schema

from voting.schemas.schema_vote import conf_schema_vote

conf_schema_professor = Schema(
    {
        "id": str,
        "name": str,
        "email": str,
        "votes": conf_schema_vote
    }
)

conf_schema_list_professors = Schema(
    {
        "count": int,
        "next": Or(None, str),
        "previous": Or(None, str),
        "results": [
            conf_schema_professor
        ]
    }
)

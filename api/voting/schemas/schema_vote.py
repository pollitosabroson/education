from schema import Or, Schema

conf_schema_vote = Schema(
    {
        "total": int,
        "average": Or(int, float)
    }
)

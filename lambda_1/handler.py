from lambda_1.src.util import get_db


db = get_db()


def handler(event, context) -> dict:
    records = event.get("Records", "")

    if records:
        db.save(records)
    return {"statusCode": 200, "body": "Hello from Lambda!"}

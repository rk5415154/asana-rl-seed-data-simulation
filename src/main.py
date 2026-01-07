import os
import uuid
from datetime import datetime

from utils.db import get_connection, execute_schema
from generators.users import generate_users


DB_PATH = "output/asana_simulation.sqlite"
SCHEMA_PATH = "schema.sql"


def main():
    os.makedirs("output", exist_ok=True)

    conn = get_connection(DB_PATH)

    # Create schema
    execute_schema(conn, SCHEMA_PATH)

    # Create organization
    organization_id = str(uuid.uuid4())
    conn.execute(
        """
        INSERT INTO organizations (organization_id, name, domain, created_at)
        VALUES (?, ?, ?, ?)
        """,
        (
            organization_id,
            "Example SaaS Corporation",
            "example.com",
            datetime.now().isoformat(),
        ),
    )
    conn.commit()

    # Generate users
    print("Generating users...")
    generate_users(conn, organization_id, num_users=200)

    conn.close()
    print("Database generation completed successfully.")


if __name__ == "__main__":
    main()


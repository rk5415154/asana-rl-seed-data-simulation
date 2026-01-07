import uuid
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()


def generate_users(conn, organization_id: str, num_users: int):
    cursor = conn.cursor()

    roles = [
        "Software Engineer",
        "Senior Engineer",
        "Product Manager",
        "Engineering Manager",
        "Designer",
        "QA Engineer",
        "Marketing Manager",
        "Operations Analyst",
    ]

    base_date = datetime.now() - timedelta(days=365)

    users = []
    for _ in range(num_users):
        user_id = str(uuid.uuid4())
        full_name = fake.name()
        email = (
            full_name.lower()
            .replace(" ", ".")
            .replace("'", "")
            + "@example.com"
        )
        role = random.choice(roles)
        joined_at = base_date + timedelta(days=random.randint(0, 300))

        users.append(
            (
                user_id,
                organization_id,
                full_name,
                email,
                role,
                joined_at.isoformat(),
            )
        )

    cursor.executemany(
        """
        INSERT INTO users (
            user_id,
            organization_id,
            full_name,
            email,
            role,
            joined_at
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        users,
    )

    conn.commit()


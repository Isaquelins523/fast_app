from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fast_app.models import User, table_registry


def test_create_users():
    engine = create_engine('sqlite:///:memory:')
    table_registry.metadata.create_all(engine)
    with Session(engine) as session:
        user = User(
            username='João',
            email='João@email.com',
            password='passwordTest',
        )
        session.add(user)
        session.commit()
        session.refresh(user)
    assert user.id == 1

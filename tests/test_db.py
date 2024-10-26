from sqlalchemy import select

from fast_app.models import User


def test_create_users(session):
    user = User(
        username='João',
        email='João@email.com',
        password='passwordTest',
    )
    session.add(user)
    session.commit()

    result = session.scalar(select(User).where(User.email == 'João@email.com'))
    assert result.username == 'João'

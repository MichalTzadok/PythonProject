import asyncio
import pytest
from app.models.user import User
from app.services import user_service

@pytest.mark.parametrize("user,expected_id, expected_name, expected_password", [
    (User(id=3, name='u', password='12345'), 3, 'u', '12345'),
    (User(id=0, name='shoshi', password='1234'), 0, 'shoshi', '1234'),
])
@pytest.mark.asyncio
async def test_login(user, expected_id, expected_name, expected_password):
    result = await user_service.login(user)
    assert result.id == expected_id
    assert result.name == expected_name
    assert result.password == expected_password

@pytest.mark.asyncio
async def test_sign_up():
    new_user = User(id=9, name='michalile', password='123456')
    result = await user_service.sign_up(new_user)
    assert result == new_user
    assert result.id is not None

@pytest.mark.asyncio
async def test_update_user_detail():
    updated_user = User(id=6, name='shoshana', password='1234')
    result = await user_service.update_user_detail(updated_user)
    assert result == updated_user


@pytest.mark.asyncio
async def test_get_user_by_id():
    user = User(id=6, name='shoshana', password='1234')
    result = await user_service.get_user_by_id(6)
    assert result == user

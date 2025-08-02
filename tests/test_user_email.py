import pytest
from httpx import AsyncClient
from fastapi import status

@pytest.mark.asyncio
async def test_login_with_invalid_email_format(async_client: AsyncClient):
    login_data = {
        "username": "not-an-email",  # OAuth2PasswordRequestForm uses "username" field
        "password": "SomePassword123"
    }

    response = await async_client.post("/auth/token", data=login_data)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert "email" in response.text.lower() or "value is not a valid email" in response.text.lower()

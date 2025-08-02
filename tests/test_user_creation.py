import pytest
from httpx import AsyncClient
from fastapi import status

@pytest.mark.asyncio
async def test_nickname_too_long(async_client: AsyncClient):
    data = {
        "email": "longnick@example.com",
        "nickname": "x" * 60,
        "first_name": "Test",
        "last_name": "User",
        "bio": "Bio",
        "profile_picture_url": None,
        "linkedin_profile_url": None,
        "github_profile_url": None,
        "role": "ANONYMOUS",
        "password": "TestPass123!"
    }
    response = await async_client.post("/users/", json=data)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert "nickname" in str(response.json())

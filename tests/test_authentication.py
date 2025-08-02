import pytest
import jwt
from datetime import datetime, timedelta
from httpx import AsyncClient
from fastapi import status
from app.dependencies import get_settings

@pytest.mark.asyncio
async def test_expired_jwt_token(async_client: AsyncClient):
    settings = get_settings()

    # Generate expired token
    expired_token = jwt.encode(
        {
            "sub": "test@example.com",
            "exp": datetime.utcnow() - timedelta(minutes=1)  # already expired
        },
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM
    )

    headers = {"Authorization": f"Bearer {expired_token}"}
    response = await async_client.get("/users/me", headers=headers)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert "expired" in response.text.lower()

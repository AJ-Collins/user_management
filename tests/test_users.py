import pytest
from httpx import AsyncClient
from fastapi import status

@pytest.mark.asyncio
async def test_standard_user_cannot_promote_to_admin(async_client: AsyncClient, standard_user_token_headers, standard_user_id):
    update_payload = {
        "role": "ADMIN"
    }

    response = await async_client.patch(
        f"/users/{standard_user_id}",
        headers=standard_user_token_headers,
        json=update_payload
    )

    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "not authorized" in response.text.lower() or "permission" in response.text.lower()

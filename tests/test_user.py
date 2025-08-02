import pytest
from httpx import AsyncClient
from fastapi import status

@pytest.mark.asyncio
async def test_update_user_email_and_verify(async_client: AsyncClient, standard_user_token_headers, standard_user_id):
    new_email = "new.email@example.com"

    # Step 1: Update user email
    response = await async_client.patch(
        f"/users/{standard_user_id}",
        headers=standard_user_token_headers,
        json={"email": new_email}
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["email"] == new_email

    # Step 2: Fetch user to confirm persistence
    get_response = await async_client.get(
        f"/users/{standard_user_id}",
        headers=standard_user_token_headers
    )

    assert get_response.status_code == status.HTTP_200_OK
    assert get_response.json()["email"] == new_email

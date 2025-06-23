import pytest



@pytest.mark.asyncio
async def test_create_user(async_client):
    response = await async_client.post("/api/v1/users/", json={
        "email": "testuser@example.com",
        "name": "Test User",
        "password": "testpassword"
    })
    assert response.status_code == 201 or response.status_code == 200
    data = response.json()
    assert data["email"] == "testuser@example.com"

@pytest.mark.asyncio
async def test_get_users(async_client):
    # Create a known user
    test_email = "test3@example.com"
    test_name = "Test User 3"

    await async_client.post("/api/v1/users/", json={
        "email": test_email,
        "name": test_name,
        "password": "testpass3"
    })

    response = await async_client.get("/api/v1/users/")
    assert response.status_code == 200

    data = response.json()

    # Find the created user by email
    user = next((u for u in data if u["email"] == test_email), None)
    assert user is not None
    assert user["name"] == test_name

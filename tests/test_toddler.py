import pytest

@pytest.mark.asyncio
async def test_create_toddler(async_client):
    user_id = 1  # You can create a user first or mock this user_id
    response = await async_client.post(
        "/api/v1/toddlers/",
        json={
            "name": "Baby Doe",
            "age_months": 12,
            "gender": "Laki-laki",
            "weight_kg": 8.5,
            "height_cm": 75.0,
            "user_id": user_id
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert "name" in data
    assert data["user_id"] == user_id
    
@pytest.mark.asyncio
async def test_get_toddlers(async_client):
    response = await async_client.get("/api/v1/toddlers/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

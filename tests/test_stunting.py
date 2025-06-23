import pytest

@pytest.mark.asyncio
async def test_predict(async_client):
    payload = {
        "name": "John Doe",
        "age_months": 24,
        "weight_kg": 10.5,
        "height_cm": 80.0,
        "gender": "Laki-laki",
        "user_id": 1
    }

    response = await async_client.post("/api/v1/predict", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    assert "gpt_response" in data



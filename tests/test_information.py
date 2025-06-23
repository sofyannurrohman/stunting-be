import pytest

@pytest.mark.asyncio
async def test_create_information(async_client):
    with open("tests/test.png", "rb") as img:
        response = await async_client.post(
            "/api/v1/information/",
            data={
                "title": "Healthy Eating",
                "content": "Eat veggies daily."
            },
            files={"image": ("test.png", img, "image/png")}
        )
    assert response.status_code == 201 or response.status_code == 200
    data = response.json()
    assert data["title"] == "Healthy Eating"

@pytest.mark.asyncio
async def test_get_information(async_client):
    response = await async_client.get("/api/v1/information/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

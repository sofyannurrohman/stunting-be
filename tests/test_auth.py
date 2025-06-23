import pytest
from httpx import AsyncClient
from passlib.context import CryptContext
from db.models.user import User
from conftest import pytest_asyncio, TestSessionLocal  # Ensure to import this correctly if needed

# Example of using passlib for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Fixture to create a test user
@pytest_asyncio.fixture
async def test_user(prepare_database):  # Assuming prepare_database fixture is available
    async with TestSessionLocal() as session:
        # Hash password and create a test user
        hashed_password = pwd_context.hash("testpassword")
        user = User(email="test@example.com", hashed_password=hashed_password)
        session.add(user)
        await session.commit()
        return user

@pytest.mark.asyncio
async def test_login_success(async_client, test_user):
    # Login with the test user
    response = await async_client.post("/api/v1/auth/login", json={
        "email": test_user.email,  # Correct field access for the User model
        "password": "testpassword"  # The plain text password to compare
    })

    # Print the response body for debugging
    print("Response Body:", response.text)

    # Check if the response status code indicates success (usually 200)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    # Get the response data
    data = response.json()

    # Assert that the 'access_token' is in the response
    assert "access_token" in data, f"Expected 'access_token' in response, got {data}"

@pytest.mark.asyncio
async def test_login_failure(async_client):
    # Try to log in with invalid credentials
    response = await async_client.post("/api/v1/auth/login", json={
        "email": "nonexistent@example.com",
        "password": "wrongpassword"
    })

    # Print the response body for debugging
    print("Response Body:", response.text)

    # Check if the response status code indicates failure (usually 400 or 401)
    assert response.status_code in [400, 401], f"Expected status code 400 or 401, got {response.status_code}"

    # Get the response data
    data = response.json()

    # Assert that the response contains the 'detail' key indicating the error message
    assert "detail" in data, f"Expected 'detail' in response, got {data}"

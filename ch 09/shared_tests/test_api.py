import pytest
import requests

# The 3 proxy target endpoints exposed by Nginx
FRAMEWORK_URLS = [
    "http://localhost/fastapi",
    "http://localhost/flask",
    "http://localhost/django"
]

@pytest.fixture(params=FRAMEWORK_URLS)
def base_url(request):
    """Dynamically yields the base URL for each framework under test."""
    return request.param


def test_get_users_pagination(base_url):
    """
    TODO: Test GET /users with page=1 and limit=10.
    Verify structural JSON layout, 200 OK status, and correct item count.
    """
    response = requests.get(f"{base_url}/users?page=1&limit=10")
    assert response.status_code == 200
    # Add validation rules over response payload dictionary mapping...


def test_create_user_validation(base_url):
    """
    TODO: Test POST /users with invalid email format or missing fields.
    Verify that ALL 3 frameworks catch validation issues and return 422 or 400.
    """
    pass


def test_user_lifecycle_crud(base_url):
    """
    TODO: Implement full end-to-end trace:
    1. POST a new valid user record -> 201 Created.
    2. GET the user by returned ID -> verify matches.
    3. PUT modify user property -> verify mutation update.
    4. DELETE user by ID -> verify 204 or 200.
    5. GET user by ID again -> verify 404 Not Found.
    """
    pass
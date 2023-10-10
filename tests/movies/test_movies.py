def test_create_movies_with_admin_user(client, admin_access_token):
    response = client.post(
        "/movies",
        headers={"Authorization": f"Bearer {admin_access_token}"},
        json=[
            {
                "99popularity": 83.0,
                "director": "Victor Fleming",
                "imdb_score": 8.3,
                "name": "The Wizard of Oz",
            }
        ],
    )
    assert response.status_code == 201, "Couldn't Create Movies with admin user"


def test_create_movies_with_authenticated_user(client, user_access_token):
    response = client.post(
        "/movies",
        headers={"Authorization": f"Bearer {user_access_token}"},
        json=[
            {
                "99popularity": 83.0,
                "director": "Victor Fleming",
                "imdb_score": 8.3,
                "name": "The Wizard of Oz",
            }
        ],
    )
    assert response.status_code == 403, "Was able to create Movie as a Normal user"

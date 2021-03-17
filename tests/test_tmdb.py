import pytest
from main import app
import tmdb_client
from unittest.mock import Mock



def test_get_poster_url_uses_default_size():
    # Przygotowanie danych
    poster_api_path = "some-poster-path"
    expected_default_size = 'w342'
    # Wywołanie kodu, który testujemy
    poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
    # Porównanie wyników
    assert expected_default_size in poster_url


def test_get_movies_list_type_popular():
   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list is not None

def some_function_to_mock():
   raise Exception("Original was called")

def test_mocking(monkeypatch):
    my_mock = Mock()
    my_mock.return_value = 2
    monkeypatch.setattr("tests.test_tmdb.some_function_to_mock", my_mock)
    result = some_function_to_mock()
    assert result == 2

def test_get_movies_list(monkeypatch):
    # Lista, którą będzie zwracać przysłonięte "zapytanie do API"
    mock_movies_list = ['Movie 1', 'Movie 2']

    requests_mock = Mock()
    # Wynik wywołania zapytania do API
    response = requests_mock.return_value
    # Przysłaniamy wynik wywołania metody .jason()
    response.json.return_value = mock_movies_list
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    movies_list = tmdb_client.get_movies_list(list_type="now_playing")
    assert movies_list == mock_movies_list


def test_get_single_movie(monkeypatch):
    mock_single_movie = ['title', 'overview', 'budget', 'genre', 'country', 'cast']

    requests_mock = Mock()

    response = requests_mock.return_value

    response.json.return_value = mock_single_movie
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    # testing id=123
    single_movie = tmdb_client.get_single_movie(movie_id=123)
    assert single_movie == mock_single_movie

def test_single_movie_cast(monkeypatch):
    mock_actor_details = ['name', 'character', 'gender']
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_actor_details
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    actor_details = tmdb_client.get_single_movie_cast(movie_id=123)
    assert actor_details == mock_actor_details 


@pytest.mark.parametrize('n, result', (
    ('top_rated', 200),
    ('upcoming', 200),
    ('popular', 200),
    ('now_playing', 200)
))

def test_homepage(monkeypatch, n, result):
    api_mock = Mock(return_value={'results': []})
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        api_mock.assert_called_once_with('movie/popular')
        

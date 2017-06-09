import pytest
import connexion

flask_app = connexion.App(__name__, specification_dir='../swagger/')
flask_app.add_api('swagger.yaml',
                  arguments={'title':
                             'The REST API for the Ophicleide Word2Vec server'})


@pytest.fixture(scope='module')
def client():
    with flask_app.app.test_client() as c:
        yield c

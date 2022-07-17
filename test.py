import pytest
import logging


@pytest.fixture(autouse=True)
def function_autouse():
    logging.info("scope function with autouse")

@pytest.fixture(scope="session")
def session():
    logging.info("scope session")


@pytest.fixture(scope="package")
def package():
    logging.info("scope package")


@pytest.fixture(scope="module")
def module():
    logging.info("scope module")


@pytest.fixture(scope="class")
def class_():
    logging.info("scope class")





def test_order(module, class_, session, function, package):
    assert True

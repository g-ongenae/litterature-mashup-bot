# content of conftest.py
import pytest


def pytest_addoption(parser):
    """
    Prepare command option addoption
    """
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
    )


@pytest.fixture
def cmdopt(request):
    """
    CLI option
    """
    return request.config.getoption("--cmdopt")

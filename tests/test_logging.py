import logging
from app.core.logging_ import setup_logging


def main():
    """Run the logging demo as a standalone script.

    This function initializes logging using the `setup_logging` function,
    creates a logger named `tests.logging`, and logs messages at different
    levels (DEBUG, INFO, WARNING).
    """
    setup_logging()
    log = logging.getLogger("tests.logging")

    log.debug("Starting test (debug)")
    log.info("Service ready (info)")
    log.warning("Slow response detected (warning)")
    # No intentional errors here


def test_logging_demo():
    """Run a logging test for pytest.

    This function sets up logging, creates a logger using the current
    module's name, and logs messages at different levels. It ends with a
    trivial assertion to ensure test execution.
    """
    setup_logging()
    log = logging.getLogger(__name__)

    log.debug("Pytest logging: debug")
    log.info("Pytest logging: info")
    log.warning("Pytest logging: warning")

    assert True


if __name__ == "__main__":
    main()

import logging
from pathlib import Path
from functools import wraps
from typing import Callable, Any


def setup_logger(
    name: str,
    level: int = logging.INFO,
) -> logging.Logger:
    """Setup logger instance.

    Args:
        name: name of the logger (usually __name__ or class name).
        level: logging level (default INFO).
        log_file: optional path to a file where logs should be written.
            If provided, a `FileHandler` with UTF-8 encoding will be added.
    """
    logger = logging.getLogger(name)

    base_dir = Path(__file__).parent.parent
    log_file = base_dir / "tests_execution.log"

    if not logger.handlers:
        std_handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        std_handler.setFormatter(formatter)
        logger.addHandler(std_handler)

        file_handler = logging.FileHandler(str(log_file), encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    logger.setLevel(level)

    return logger


def log_action(action_name: str) -> Callable:
    """Decorator for logging actions"""

    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(self, *args, **kwargs):
            class_logger = setup_logger(self.__class__.__name__)

            class_logger.info("Starting: %s", action_name)

            try:
                result = func(self, *args, **kwargs)
                class_logger.info("%s result: %s", action_name, result)
                return result

            except Exception as e:
                class_logger.error(
                    "Failed: %s | %s: %s",
                    action_name,
                    type(e).__name__,
                    str(e),
                )
                raise

        return wrapper

    return decorator


if __name__ == "__main__":
    # один глобальний logger
    logger = setup_logger("app_logger")

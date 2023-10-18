import logging

logger = logging.getLogger(__name__)


def str2bool(x: str) -> bool:
    """Cast string to boolean.

    Useful for parsing command line arguments.
    """
    if not isinstance(x, str):
        raise TypeError("String expected.")
    elif x.lower() in ("true", "t", "1"):
        return True
    elif x.lower() in ("false", "f", "0"):
        return False
    else:
        raise ValueError(f"'{x}' does not seem to be boolean.")

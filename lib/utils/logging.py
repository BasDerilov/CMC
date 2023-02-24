def started(message: str):
    """log started

    Args:
        message (str): text message to print
    """
    print(_bcolors.OKBLUE + f"| ::: {message.lower()} ::: |" + _bcolors.ENDC)


def success(message: str):
    """log success

    Args:
        message (str): text message to print
    """
    print(_bcolors.OKGREEN + f"< ::: {message.lower()} ::: >" + _bcolors.ENDC)


def failure(message: str):
    """log failure

    Args:
        message (str): text message to print
    """
    print(_bcolors.FAIL + f"X ::: {message.lower()} ::: X" + _bcolors.ENDC)


def warning(message: str):
    """log warning

    Args:
        message (str): text message to print
    """
    print(_bcolors.WARNING + f"! ::: {message.lower()} ::: !" + _bcolors.ENDC)


class _bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"

    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

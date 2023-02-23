def started(message: str):
    print(_bcolors.OKBLUE + f"| ::: {message.lower()} ::: |" + _bcolors.ENDC)


def success(message: str):
    print(_bcolors.OKGREEN + f"< ::: {message.lower()} ::: >" + _bcolors.ENDC)


def failure(message: str):
    print(_bcolors.FAIL + f"X ::: {message.lower()} ::: X" + _bcolors.ENDC)
    raise Exception(message)


def warning(message: str):
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

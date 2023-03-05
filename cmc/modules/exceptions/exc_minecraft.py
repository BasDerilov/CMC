class MissingApiToken(Exception):
    """A required API access token is missing"""


class InvalidApiToken(Exception):
    """The configured API token is incorrect or has insufficient access"""


class CurseResourceNotFound(Exception):
    """The requested curse resource was not found"""


class MissingEnvVariable(Exception):
    """A required environmental variable is missing"""

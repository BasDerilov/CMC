"""Top-level package for gcp_mc."""

__app_name__ = "gcp-mc"
__version__ = "0.9.0"


(
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
) = range(3)

ERRORS = {
    DIR_ERROR: "config directory error",
    FILE_ERROR: "config file error",
}

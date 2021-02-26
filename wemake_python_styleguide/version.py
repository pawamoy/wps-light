from wemake_python_styleguide.compat.packaging import (
    PackageNotFoundError,
    get_version,
)


def _get_version(dist_name: str) -> str:  # pragma: no cover
    """Fetches distribution version."""
    try:
        return get_version(dist_name)
    except PackageNotFoundError:
        return ''  # readthedocs cannot install `poetry` projects


#: This is a package name.
pkg_name = 'wps-light'

#: We store the version number inside the `pyproject.toml`.
pkg_version = _get_version(pkg_name)

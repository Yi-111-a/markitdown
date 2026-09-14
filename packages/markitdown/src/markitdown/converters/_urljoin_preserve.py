"""urljoin wrapper that keeps empty interior path segments.

CPython's urllib.parse.urljoin drops empty segments, so
``exports/2026//report.csv`` becomes ``exports/2026/report.csv``.
Object-store paths can treat those slashes as significant.
"""

from urllib.parse import urljoin, urlsplit, urlunsplit

# Placeholder for an empty path segment. Unlikely to appear in a real URL.
_EMPTY_PATH_SEGMENT = "\ufffc"


def _protect_empty_path_segments(url: str) -> str:
    parts = urlsplit(url)
    if not parts.path or "//" not in parts.path:
        return url
    segments = parts.path.split("/")
    last = len(segments) - 1
    protected = [
        _EMPTY_PATH_SEGMENT if (segment == "" and i not in (0, last)) else segment
        for i, segment in enumerate(segments)
    ]
    return urlunsplit(
        (parts.scheme, parts.netloc, "/".join(protected), parts.query, parts.fragment)
    )


def resolve_url(base_url: str, reference: str) -> str:
    """Resolve a reference without collapsing significant repeated slashes."""
    try:
        return urljoin(
            _protect_empty_path_segments(base_url),
            _protect_empty_path_segments(reference),
        ).replace(_EMPTY_PATH_SEGMENT, "")
    except ValueError:
        return reference

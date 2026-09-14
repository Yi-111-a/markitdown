import io

from markitdown import MarkItDown, StreamInfo
from markitdown.converters._urljoin_preserve import resolve_url


def test_resolve_url_keeps_repeated_slashes() -> None:
    assert (
        resolve_url(
            "https://example.com/bucket/",
            "exports/2026//report.csv",
        )
        == "https://example.com/bucket/exports/2026//report.csv"
    )
    assert resolve_url("https://example.com/a//b/", "c") == "https://example.com/a//b/c"


def test_rss_html_link_keeps_repeated_slashes() -> None:
    feed = b"""<rss version=\"2.0\"><channel>
<title>Exports</title><link>https://example.com/bucket/</link>
<description>Available reports</description>
<item><title>Report</title><description><![CDATA[
<a href=\"exports/2026//report.csv\">Download</a>
]]></description></item>
</channel></rss>"""

    result = MarkItDown().convert_stream(
        io.BytesIO(feed),
        stream_info=StreamInfo(
            extension=".rss",
            charset="utf-8",
            url="https://example.com/bucket/feed.xml",
        ),
    )

    assert (
        "[Download](https://example.com/bucket/exports/2026//report.csv)"
        in result.markdown
    )
    assert "exports/2026/report.csv" not in result.markdown

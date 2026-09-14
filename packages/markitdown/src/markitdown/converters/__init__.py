# SPDX-FileCopyrightText: 2024-present Adam Fourney <adamfo@microsoft.com>
#
# SPDX-License-Identifier: MIT

from ._plain_text_converter import PlainTextConverter
from ._html_converter import HtmlConverter
from ._rss_converter import RssConverter
from ._wikipedia_converter import WikipediaConverter
from ._youtube_converter import YouTubeConverter
from ._ipynb_converter import IpynbConverter
from ._bing_serp_converter import BingSerpConverter
from ._pdf_converter import PdfConverter
from ._docx_converter import DocxConverter
from ._xlsx_converter import XlsxConverter, XlsConverter
from ._pptx_converter import PptxConverter
from ._image_converter import ImageConverter
from ._audio_converter import AudioConverter
from ._outlook_msg_converter import OutlookMsgConverter
from ._zip_converter import ZipConverter
from ._doc_intel_converter import (
    DocumentIntelligenceConverter,
    DocumentIntelligenceFileType,
)
from ._cu_converter import (
    ContentUnderstandingConverter,
    ContentUnderstandingFileType,
)
from ._epub_converter import EpubConverter
from ._csv_converter import CsvConverter
from . import _rss_converter as _rss_converter_module
from ._urljoin_preserve import resolve_url as _preserve_feed_urljoin

# urllib.parse.urljoin collapses empty path segments. Replace the RSS helper
# so feed links keep significant repeated slashes (see #2468).
_rss_converter_module._resolve_url = _preserve_feed_urljoin

__all__ = [
    "PlainTextConverter",
    "HtmlConverter",
    "RssConverter",
    "WikipediaConverter",
    "YouTubeConverter",
    "IpynbConverter",
    "BingSerpConverter",
    "PdfConverter",
    "DocxConverter",
    "XlsxConverter",
    "XlsConverter",
    "PptxConverter",
    "ImageConverter",
    "AudioConverter",
    "OutlookMsgConverter",
    "ZipConverter",
    "DocumentIntelligenceConverter",
    "DocumentIntelligenceFileType",
    "ContentUnderstandingConverter",
    "ContentUnderstandingFileType",
    "EpubConverter",
    "CsvConverter",
]

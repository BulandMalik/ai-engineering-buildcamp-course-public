import html
import json
import re
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

TAG_RE = re.compile(r"<[^>]+>")


class SearchWikipediaTool:
    """Search English Wikipedia and return matching pages.

    Use this when you have a query and need matching page titles.
    Pass a search string such as "capybara", not an exact page title.
    To read one article after you know its title, use get_page instead.

    Args:
        query: Text to search for in page titles and content.
        limit: How many hits to request per API page. Default is 10.
            Allowed range is 1 to 500.
        cap: Stop after this many hits so a broad query cannot page
            forever. Default is 50.

    Returns:
        dict: {"total": int, "hits": list[dict]}.
        total is every matching page on Wikipedia (searchinfo.totalhits).
        hits are the pages actually collected, each with title, pageid,
        wordcount, timestamp, and a plain-text snippet.
        An empty query returns {"total": 0, "hits": []}.

    Raises:
        RuntimeError: Wikipedia could not be reached or returned an API error.
    """

    name = "search_wikipedia"
    description = (
        "Search English Wikipedia by query text. "
        "Argument query is a string such as 'capybara', not an exact page title. "
        "Optional limit is the page size (default 10) and optional cap is the "
        "maximum hits to collect (default 50). "
        "Returns a dict with total, the full match count, and hits, a list of "
        "title, pageid, wordcount, timestamp, and snippet."
    )

    API_URL = "https://en.wikipedia.org/w/api.php"
    USER_AGENT = "WikipediaAgent/0.1 (week 3 homework; course project)"
    TIMEOUT = 20
    PAGE_SIZE = 10
    MAX_HITS = 50
    verbose = False

    def __init__(self, verbose: bool = False):
        self.verbose = verbose

    def search_wikipedia(
        self,
        query: str,
        limit: int = PAGE_SIZE,
        cap: int = MAX_HITS,
    ) -> dict:
        """Search Wikipedia. Same arguments and return value as SearchWikipediaTool."""
        query = query.strip()
        if not query:
            return {"total": 0, "hits": []}

        hits = []
        total = 0
        offset = 0

        while True:
            data = self._fetch_page(query, offset, limit)
            if "error" in data:
                info = data["error"].get("info", "search error")
                raise RuntimeError(info)

            search = data.get("query", {}).get("search", [])
            total = data.get("query", {}).get("searchinfo", {}).get("totalhits", total)

            for item in search:
                hits.append({
                    "title": item["title"],
                    "pageid": item["pageid"],
                    "wordcount": item.get("wordcount"),
                    "timestamp": item.get("timestamp"),
                    "snippet": self._plain_snippet(item.get("snippet", "")),
                })
                if len(hits) >= min(total, cap):
                    return {"total": total, "hits": hits}

            cont = data.get("continue")
            if not cont or not search:
                break
            offset = cont["sroffset"]

        return {"total": total, "hits": hits}

    def __call__(
        self,
        query: str,
        limit: int = PAGE_SIZE,
        cap: int = MAX_HITS,
    ) -> dict:
        """Search English Wikipedia and return matching pages.

        Args:
            query: Text to search for, for example "capybara".
                This is not an exact page title.
            limit: Hits to request per API page. Default is 10.
            cap: Maximum hits to collect. Default is 50.

        Returns:
            dict: {"total": int, "hits": list[dict]}.
            total is the full match count. hits are the collected pages,
            each with title, pageid, wordcount, timestamp, and snippet.
        """
        return self.search_wikipedia(query, limit=limit, cap=cap)

    def _fetch_page(self, query: str, offset: int, limit: int) -> dict:
        params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "srlimit": limit,
            "sroffset": offset,
            "srnamespace": 0,
            "srinfo": "totalhits",
            "srprop": "size|wordcount|timestamp|snippet",
            "format": "json",
        }
        url = f"{self.API_URL}?{urlencode(params)}"
        request = Request(url, headers={"User-Agent": self.USER_AGENT})

        try:
            with urlopen(request, timeout=self.TIMEOUT) as response:
                status = response.status
                data = json.loads(response.read().decode("utf-8"))
        except (URLError, TimeoutError) as err:
            raise RuntimeError(
                f"Could not reach {self.API_URL}. "
                f"Check your internet connection. ({err})"
            ) from err

        if self.verbose:
            print(f"URL: {request.full_url}")
            print(f"Request: {request.get_method()} {request.full_url}")
            print(f"Response: {status}")
            print(json.dumps(data, indent=2))
        return data

    def _plain_snippet(self, text: str) -> str:
        return html.unescape(TAG_RE.sub("", text))

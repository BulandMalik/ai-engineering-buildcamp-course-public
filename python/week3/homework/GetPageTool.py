import json
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


class GetPageTool:
    """Count the characters in one English Wikipedia page.

    Use this when the exact page title is already known.
    Pass a title such as "Capybara", not a search query.
    The article is read here. Only the character count is returned.

    Args:
        title: Exact Wikipedia page title.

    Returns:
        int: Number of characters in the full article. 0 means the title
        was blank or the page does not exist.

    Raises:
        RuntimeError: Wikipedia could not be reached or returned an API error.
    """

    name = "get_page"
    description = (
        "Read one English Wikipedia page by its exact title and return only "
        "the character count as an integer. Argument title is a string such as "
        "'Capybara', not a search query. The article text is not returned."
    )

    API_URL = "https://en.wikipedia.org/w/api.php"
    USER_AGENT = "WikipediaAgent/0.1 (week 3 homework; course project)"
    TIMEOUT = 20
    # Plain text of the Capybara article is about 15,000 characters.
    # The raw wikitext is about 200,000. This cap keeps the model request
    # on the plain-text excerpt.
    EXCERPT_CHARS = 16000
    verbose = False

    def __init__(self, verbose: bool = False):
        self.verbose = verbose

    def _query(self, params: dict) -> dict:
        params = {**params, "format": "json"}
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
        if "error" in data:
            info = data["error"].get("info", "get page error")
            raise RuntimeError(info)
        return data

    def get_page(self, title: str) -> int:
        """Read one Wikipedia page and return only its character count."""
        title = title.strip()
        if not title:
            return 0

        data = self._query({
            "action": "query",
            "prop": "revisions",
            "titles": title,
            "rvprop": "content",
            "rvslots": "main",
            "formatversion": "2",
            "redirects": "1",
        })
        pages = data.get("query", {}).get("pages", [])
        if not pages or "missing" in pages[0]:
            return 0

        content = pages[0]["revisions"][0]["slots"]["main"]["content"]
        return len(content)

    def get_excerpt(self, title: str) -> str:
        """Return plain text from one Wikipedia page for the model to read.

        The article is fetched as plain text, not wikitext, and cut at
        EXCERPT_CHARS. The model receives this excerpt and nothing else.

        Args:
            title: Exact Wikipedia page title, for example "Capybara".
                This is not a search query.

        Returns:
            str: Plain-text excerpt. An empty string means the title was
            blank or the page does not exist.
        """
        title = title.strip()
        if not title:
            return ""
        data = self._query({
            "action": "query",
            "prop": "extracts",
            "explaintext": 1,
            "titles": title,
            "redirects": 1,
            "formatversion": 2,
        })
        pages = data.get("query", {}).get("pages", [])
        if not pages or "missing" in pages[0]:
            return ""
        text = pages[0].get("extract") or ""
        if len(text) > self.EXCERPT_CHARS:
            text = text[:self.EXCERPT_CHARS]
        return text

    def __call__(self, title: str) -> int:
        """Read one Wikipedia page and return only its character count.

        Args:
            title: Exact Wikipedia page title, for example "Capybara".
                This is not a search query.

        Returns:
            int: Number of characters in the full article. 0 means the title
            was blank or the page does not exist.
        """
        return self.get_page(title)

# Week 3 Homework: Building a Wikipedia Agent

A small agent that searches English Wikipedia. This first version does three things:

1. Search with a query.
2. Read how many pages match.
3. Walk the result pages and collect each hit.

Full page text and generated answers come later. This version only talks to the search API.

API reference: [API:Search](https://www.mediawiki.org/wiki/API:Search)

## Endpoint

```
GET https://en.wikipedia.org/w/api.php
```

Search is a read-only `query` list. No login and no API key.

Send a `User-Agent` header that names this homework and a way to reach you. Wikimedia rejects clients that look like anonymous scripts.

```
User-Agent: WikipediaAgent/0.1 (week 3 homework; your-email@example.com)
```

## Search with a query

Required parameters:

| Parameter | Value | Why |
| --- | --- | --- |
| `action` | `query` | MediaWiki Action API |
| `list` | `search` | Full-text search module (`sr`) |
| `srsearch` | the query string | Required. Matches page titles and content |
| `format` | `json` | Parse the body as JSON |

Useful on the first call:

| Parameter | Value | Why |
| --- | --- | --- |
| `srlimit` | `10` | Page size. Allowed range is 1–500. Default is 10 |
| `srnamespace` | `0` | Article namespace only. This is the default |
| `srinfo` | `totalhits` | Ask for the match count. Default also includes `suggestion` and `rewrittenquery` |
| `srprop` | `size\|wordcount\|timestamp\|snippet` | Default fields on each hit |

Example for the query `Nelson Mandela`:

```
https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=Nelson%20Mandela&srlimit=10&format=json
```

`srsearch` follows the wiki's search syntax. On English Wikipedia that is [CirrusSearch](https://www.mediawiki.org/wiki/Help:CirrusSearch). A plain string is enough here.

## Find the total

The count lives at `query.searchinfo.totalhits`. It is the number of matching pages, which is larger than the page you just received.

```json
{
  "query": {
    "searchinfo": {
      "totalhits": 5060
    }
  }
}
```

Read `totalhits` once, from the first response, and keep it. Later pages repeat the same count.

If `srsearch` is missing, the API returns `nosrsearch`.

## Iterate the results

Each response holds one page of hits in `query.search`. A hit looks like this:

```json
{
  "ns": 0,
  "title": "Nelson Mandela",
  "pageid": 21492751,
  "size": 196026,
  "wordcount": 23664,
  "snippet": "Nelson Rolihlahla Mandela ... was a South African anti-apartheid revolutionary,",
  "timestamp": "2018-07-23T07:59:43Z"
}
```

`snippet` contains `<span class="searchmatch">` tags around the matched words. Strip those tags before printing or storing the text.

When more hits exist, the response includes `continue`:

```json
{
  "continue": {
    "sroffset": 10,
    "continue": "-||"
  }
}
```

Pass those values back on the next request. `sroffset` is how many hits to skip. With `srlimit=10`, the offsets are `0`, then `10`, then `20`, and so on.

Stop when any of these is true:

- The response has no `continue` object. `batchcomplete` is set on that last page.
- You have collected `totalhits` items.
- You hit a cap you chose, so a huge query cannot page forever. Start with something like 50 hits.

```text
offset = 0
limit = 10
cap = 50
hits = []

loop:
    response = search(query, offset, limit)
    total = response.query.searchinfo.totalhits
    append each item in response.query.search to hits
    if no response.continue or len(hits) >= min(total, cap):
        stop
    offset = response.continue.sroffset
```

For each kept hit, record `title`, `pageid`, `wordcount`, `timestamp`, and the plain-text `snippet`. Print the total, then print one line per hit: rank, title, page id.

That is the whole first version. The agent can search, report how many pages matched, and list the pages it walked.

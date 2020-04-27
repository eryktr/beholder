from beholder.analyzer.site import Site
from beholder.fetcher.fetcher import WebFetcher


class Downloader:
    fetcher: WebFetcher

    def __init__(self, fetcher: WebFetcher):
        self.fetcher = fetcher

    def download_reference(self, site: Site) -> None:
        self.fetcher.fetch(site.addr, site.latest_path)

    def download_updated(self, site: Site) -> None:
        self.fetcher.fetch(site.addr, site.chall_path)

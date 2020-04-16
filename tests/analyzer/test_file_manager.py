from beholder.analyzer.file_manager import FileManager


def test_file_manager_latest_path():
    sites = ["http://a.pl", "http://b.pl", "http://c.pl",
             "https://d.pl", "https://e.pl", "http://f.pl"]
    manager = FileManager(sites)
    assert str(manager.latest_path(sites[3]).name) == "3o.html"


def test_file_manager_chall_path():
    sites = ["http://a.pl", "http://b.pl", "http://c.pl",
             "https://d.pl", "https://e.pl", "http://f.pl"]
    manager = FileManager(sites)
    assert str(manager.chall_path(sites[0]).name) == "0n.html"

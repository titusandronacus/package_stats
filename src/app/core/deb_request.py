from io import StringIO
import gzip

import requests


def get_deb_contents_from_url(contents_url: str) -> StringIO:
    """
    Get a zipped file from a given url, decompress it, and return it in memory file
    :param contents_url: url to download the zipped file from
    :return: StringIO object of the decompressed file.
    """
    # print(f"[bold green]Getting file from[/bold green] {contents_url}")
    r = requests.get(contents_url)
    r.raise_for_status()

    decompressed_contents = gzip.decompress(r.content)

    # TODO: probably need to decode with known encoding, but plain text is plain text
    output = StringIO(decompressed_contents.decode())

    # print("[bold green]Successfully got file")
    return output


def get_arch_contents_url(arch: str, repo_url: str):
    """
    Get the url for the contents file for the specified arch
    :param arch: arch to retrieve contents file for
    :param repo_url: url for the package repo
    :return: url
    """
    if not repo_url.endswith('/'):
        repo_url = repo_url + '/'

    # TODO: this would be a good place to validate its an actual url
    return repo_url + "Contents-" + arch + ".gz"

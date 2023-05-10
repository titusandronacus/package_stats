#!/usr/bin/env python3

from collections import defaultdict

from .deb_request import get_deb_contents_from_url, get_arch_contents_url


def get_packages_file_count(arch: str, repo_url='http://ftp.uk.debian.org/debian/dists/stable/main'):
    """
    Get the top 10 packages with the most files listed within a given arch's content file from a package rep
    """

    url = get_arch_contents_url(arch, repo_url)
    # print("1", url)  # debug

    contents = get_deb_contents_from_url(url)
    # print("2")  # debug

    tally_dict = defaultdict(int)

    for line in contents:
        # according to https://wiki.debian.org/DebianRepository/Format?action=show&redirect=RepositoryFormat#A.22Contents.22_indices
        # file names could have whitespace in them, but packages dont.
        file_name, packages = line.rsplit(' ', maxsplit=1)

        # there could be multiple packages that have the same file
        for package in packages.split(','):
            tally_dict[package.strip()] += 1

    return dict(sorted(tally_dict.items(), key=lambda item: item[1], reverse=True))


if __name__ == "__main__":
    for i, (package, file_count) in enumerate(get_packages_file_count('amd64').items(), start=1):
        print(i, package, file_count)
        if i >= 10:
            break

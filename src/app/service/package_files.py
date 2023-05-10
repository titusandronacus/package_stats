from ..core import get_packages_file_count


def get_package_files():
    files = get_packages_file_count('amd64')
    return files

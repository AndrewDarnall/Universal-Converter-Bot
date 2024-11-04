""" Module for Utility functions """

from os.path import splitext, basename


def get_basename(full_path: str) -> str:
    """
    get_basename: Wrapper for the os.pat.basename method
    """
    base = basename(full_path)
    return base


def replace_file_extension(file_path: str, new_extension: str) -> str:
    """
    replace_file_extension: Replaces the input file's extension
                            (hello.odt -> hello.pdf)
    @param file_path: The input file's PATH
    @param new_extension: The target extension
    """
    base = splitext(file_path)[0]
    new_file_path = f"{base}.{new_extension.lstrip('.')}"
    return new_file_path

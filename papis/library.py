import os
import glob
from typing import List


class Library:

    def __init__(self, name: str, paths: List[str]):
        assert(isinstance(name, str)), '`name` must be a string'
        assert(isinstance(paths, list)), '`paths` must be a list'
        self.name = name
        self.paths = sum(
            [glob.glob(os.path.expanduser(p)) for p in paths],
            [])  # type: List[str]

    def path_format(self) -> str:
        return ":".join(self.paths)

    def __str__(self) -> str:
        return self.name


def from_paths(paths: List[str]) -> Library:
    name = ":".join(paths)
    return Library(name, paths)

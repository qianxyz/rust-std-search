import os
import glob
from bs4 import BeautifulSoup

from crawl import OUTPUT_DIR as HTML_DIR


def _main():
    parse_fns = {
        "index": parse_index,
        "primitive": parse_primitive,
        "macro": parse_macro,
        "keyword": parse_keyword,
        "struct": parse_struct,
        "enum": parse_enum,
        "constant": parse_constant,
        "trait": parse_trait,
        "fn": parse_fn,
        "type": parse_type,
        "union": parse_union,
        "attr": parse_attr,
        "derive": parse_derive,
    }

    paths = glob.iglob(os.path.join(HTML_DIR, "**/*.html"), recursive=True)

    for path in paths:
        # list of all items, not interesting
        if path == os.path.join(HTML_DIR, "all.html"):
            continue

        basename = os.path.basename(path)

        parser = None
        for prefix, fn in parse_fns.items():
            if basename.startswith(prefix):
                parser = fn
                break

        if parser is None:
            raise ValueError(f"unknown file: {path}")

        with open(path) as f:
            soup = BeautifulSoup(f, "html.parser")

        parser(path, soup)


def parse_index(path, soup):
    print(f"index: {path}")


def parse_primitive(path, soup):
    print(f"primitive: {path}")


def parse_macro(path, soup):
    print(f"macro: {path}")


def parse_keyword(path, soup):
    print(f"keyword: {path}")


def parse_struct(path, soup):
    print(f"struct: {path}")


def parse_enum(path, soup):
    print(f"enum: {path}")


def parse_constant(path, soup):
    print(f"constant: {path}")


def parse_trait(path, soup):
    print(f"trait: {path}")


def parse_fn(path, soup):
    print(f"fn: {path}")


def parse_type(path, soup):
    print(f"type: {path}")


def parse_union(path, soup):
    print(f"union: {path}")


def parse_attr(path, soup):
    print(f"attr: {path}")


def parse_derive(path, soup):
    print(f"derive: {path}")


if __name__ == "__main__":
    _main()

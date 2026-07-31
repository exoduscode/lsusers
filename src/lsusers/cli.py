from __future__ import annotations

import argparse
import sys
from typing import List, Optional

from . import __version__
from .formatters import as_csv, as_json, as_names, as_table
from .platforms import UnsupportedPlatformError
from .users import filter_users, list_users


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="lsusers", description="List Linux and macOS user accounts simply"
    )
    parser.add_argument("command", nargs="?", choices=["all", "human", "system", "count"], default="human")
    output = parser.add_mutually_exclusive_group()
    output.add_argument("--json", action="store_true", help="output JSON")
    output.add_argument("--csv", action="store_true", help="output CSV")
    output.add_argument("--names", action="store_true", help="output usernames only")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        users = list_users()
    except UnsupportedPlatformError as error:
        print("lsusers: error: {}".format(error), file=sys.stderr)
        return 1

    if args.command == "human":
        users = filter_users(users, "human")
    elif args.command == "system":
        users = filter_users(users, "system")
    elif args.command == "count":
        human = len(filter_users(users, "human"))
        system = len(filter_users(users, "system"))
        print(f"human: {human}\nsystem: {system}\ntotal: {len(users)}")
        return 0

    if args.json:
        print(as_json(users))
    elif args.csv:
        print(as_csv(users))
    elif args.names:
        print(as_names(users))
    else:
        print(as_table(users))
    return 0


if __name__ == "__main__":
    sys.exit(main())

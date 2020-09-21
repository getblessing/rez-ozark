
import sys
import argparse
from . import util


def party(opt):
    if opt.init:
        util.init()
    else:
        if opt.list:
            util.ls(location=opt.at)
        else:
            util.build(location=opt.at)


def make_parsers():
    parser = argparse.ArgumentParser(description="Ozark, project profile tool")
    subparsers = parser.add_subparsers(help="sub-command help")

    # - party
    parser_party = subparsers.add_parser("party", help="Manage profiles.")
    parser_party.add_argument(
        "--init",
        action="store_true",
        help="Start creating profile with a template. Other options will "
             "be ignored if this presented."
    )
    parser_party.add_argument(
        "--at",
        help="Set profile location to write to or `--list` from."
    )
    parser_party.add_argument(
        "--list",
        action="store_true",
        help="List profiles."
    )
    # (TODO) Add an option to list out current registered locations

    return {
        "main": parser,
        "party": parser_party,
    }


def main(argv=None):
    argv = argv or sys.argv

    parsers = make_parsers()
    parser = parsers["main"]
    parser_party = parsers["party"]

    parser_party.set_defaults(run=party)

    # Parsing args
    opt = parser.parse_args(argv[1:])
    opt.run(opt)

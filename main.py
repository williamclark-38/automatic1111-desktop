"""Automatic1111 Desktop — Keep Automatic1111 workspace folders on disk: dated copies of model and prompt files before a patch."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='automatic1111_desktop',
        description='Keep Automatic1111 workspace folders on disk: dated copies of model and prompt files before a patch.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Automatic1111 Desktop')
    print('Archive Automatic1111 files on this machine before you change the install.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

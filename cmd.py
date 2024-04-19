import argparse


def print_banner():
    print(r"""
██████╗  ██╗ ██╗   ██╗      ██╗    ██╗  ██████╗  ██████╗  ██████╗  ██████╗  ██████╗  ███████╗ ███████╗ ███████╗
██╔══██╗ ██║ ██║   ██║      ██║    ██║ ██╔═══██╗ ██╔══██╗ ██╔══██╗ ██╔══██╗ ██╔══██╗ ██╔════╝ ██╔════╝ ██╔════╝
██║  ██║ ██║ ██║   ██║      ██║ █╗ ██║ ██║   ██║ ██████╔╝ ██║  ██║ ██████╔╝ ██████╔╝ █████╗   ███████╗ ███████╗
██║  ██║ ██║ ██║   ██║      ██║███╗██║ ██║   ██║ ██╔══██╗ ██║  ██║ ██╔═══╝  ██╔══██╗ ██╔══╝   ╚════██║ ╚════██║
██████╔╝ ██║ ╚██████╔╝ ▄█╗  ╚███╔███╔╝ ╚██████╔╝ ██║  ██║ ██████╔╝ ██║      ██║  ██║ ███████╗ ███████║ ███████║
╚═════╝  ╚═╝  ╚═════╝  ╚═╝   ╚══╝╚══╝   ╚═════╝  ╚═╝  ╚═╝ ╚═════╝  ╚═╝      ╚═╝  ╚═╝ ╚══════╝ ╚══════╝ ╚══════╝
                                                                   │ Author: f4tb3e   version: 0.1.0 │
                                                                   └─────────────────────────────────┘
""")


def get_args():
    parser = argparse.ArgumentParser(
        prog="Beedle",
        description="A Tool to Exploit.",
        add_help=True
    )

    # parser.add_argument(
    #     "-m", "--mode",
    #     choices=["scan", "exp"],
    #     help=(
    #         "[scan] Check target(s) are vulnerable or not, "
    #         "[exp] Exploit vulnerability on target(s)"
    #     )
    # )

    target = parser.add_mutually_exclusive_group(required=True)

    target.add_argument(
        "-u", "--url",
        type=str,
        help="URL of the target"
    )

    target.add_argument(
        "-f", "--file",
        type=str,
        help="Path to the file that contains URLs of targets"
    )

    parser.add_argument(
        "-p", "--poc",
        type=str,
        default="poc/CVE-2023-50917.yml",
        help="Choose the POC you want"
    )

    args = parser.parse_args()
    return args

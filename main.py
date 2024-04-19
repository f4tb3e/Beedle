import cmd

from obj.exploit import Exploit


def main():
    cmd.print_banner()
    args = cmd.get_args()

    exp = Exploit(args)


if __name__ == "__main__":
    main()

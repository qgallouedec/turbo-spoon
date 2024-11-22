import argparse
import os
import sys

from accelerate.commands.launch import launch_command_parser, launch_command

from trl.scripts.dpo import make_parser as make_dpo_parser


def main():
    parser = argparse.ArgumentParser("My CLI tool", usage="trl", allow_abbrev=False)

    # Add the subparsers
    subparsers = parser.add_subparsers(help="available commands", dest="command")

    # Add the subparsers for every script
    make_dpo_parser(subparsers)

    # Parse the arguments
    args = parser.parse_args()

    if args.command == "dpo":
        # Get the default args for the launch command
        dpo_training_script = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scripts", "dpo.py")
        args = launch_command_parser().parse_args([dpo_training_script])

        # Feed the args to the launch command
        args.training_script_args = sys.argv[2:]  # remove "trl" and "dpo"

        # Launch the training
        launch_command(args)


if __name__ == "__main__":
    main()

import argparse

from accelerate import Accelerator


def main(training_args):
    # Code to be run with accelerate launch
    print(training_args, Accelerator().process_index)


def make_parser(subparsers=None):
    if subparsers is not None:
        parser = subparsers.add_parser("dpo", help="Run the DPO training script")
    else:
        parser = argparse.ArgumentParser(description="Some base arguments")

    parser.add_argument("--arg1", type=str, help="The first argument")

    if subparsers is not None:
        parser.set_defaults(func=main)
    return parser


if __name__ == "__main__":
    parser = make_parser()
    args = parser.parse_args()
    main(args)

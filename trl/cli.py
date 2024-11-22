import argparse
import sys
from trl.scripts.dpo import main as dpo_main
from transformers import HfArgumentParser, TrainingArguments


def main():
    parser = argparse.ArgumentParser(prog="trl", description="A CLI tool for training and fine-tuning")
    subparsers = parser.add_subparsers(dest="command", required=True, parser_class=HfArgumentParser)

    # 'dpo' subcommand
    dpo_parser = subparsers.add_parser("dpo", help="Run the DPO training process", dataclass_types=TrainingArguments)

    args = parser.parse_args()
    sys.argv = sys.argv[1:]  # Remove 'ts' from sys.argv

    if args.command == "dpo":

        (training_args,) = dpo_parser.parse_args_into_dataclasses()
        dpo_main(training_args)

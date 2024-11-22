from transformers import HfArgumentParser, TrainingArguments


def main(training_args: TrainingArguments):
    # Code to be run with accelerate launch
    print(training_args)


if __name__ == "__main__":
    parser = HfArgumentParser(TrainingArguments)
    (training_args,) = parser.parse_args_into_dataclasses()
    main(training_args)


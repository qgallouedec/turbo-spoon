## Usage

```
pip install git+https://github.com/qgallouedec/turbo-spoon.git
```


## Demo

### Normal usage

With two GPUs, you get the script spawned on two processes:

```
$ trl dpo --arg1 my_value
Namespace(arg1='my_value') Process index: 0
Namespace(arg1='my_value') Process index: 1
```

### Help

#### Base help

```
$ trl --help
usage: trl

positional arguments:
  {dpo}       available commands
    dpo       Run the DPO training script

options:
  -h, --help  show this help message and exit
```

#### DPO help

```
$ trl dpo --help
usage: trl dpo [-h] [--arg1 ARG1]

options:
  -h, --help   show this help message and exit
  --arg1 ARG1  The first argument
```

### Argument not supported

```
$ trl dpo --arg2 my_value
usage: trl
My CLI tool: error: unrecognized arguments: --arg2 my_value
```

### Command not supported

```
$ trl abc
usage: trl
My CLI tool: error: argument command: invalid choice: 'abc' (choose from 'dpo')
```
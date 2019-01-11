# Random Username Generator

A package to randomly generate compelling usernames in the format `<adjective><noun><number>`.

Inspiration from [marstr](https://github.com/marstr/randname).

## Installation

You can install the Random Username Generator from [PyPI](https://pypi.org/project/random-username/#description):

    pip install random-username

This package is supported on Python 2.7, as well as Python 3.5 and above.

## How to use

This is a command-line application to generate usernames. To use, simply call:

    $ random_username -h
    usage: random_username [-h] [num_results]

    Generate Compelling Usernames.

    positional arguments:
    num_results  Number of results to return

    optional arguments:
    -h, --help   show this help message and exit

To generate usernames, call the program like so (not specifying a number will default to 1):

    $ random_username 10
    vengefulSausage3
    pacifiedIcecream7
    amazedOtter4
    lovesickSardines2
    grizzledChowder1
    grumpyRat1
    troubledCod7
    dopeyPiglet7
    dreadfulOtter4
    giddyOil7

You can also call the Random Username Generator from your own python code by importing from `random_username.generate`

    >>> from random_username.generate import generate_username
    >>> generate_username(5)
    ['insecureJaguar0', 'spiritedMuesli8', 'cautiousSmelt2', 'mereVenison4', 'offendedPie6']
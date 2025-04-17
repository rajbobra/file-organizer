import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--path',
        required=True,
        help='Directory you wish to organize'
    )

    parser.add_argument(
        '--config',
        required=True,
        help='Configuration file of the format in README'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Set to true if you want to see simulation of the organization without actually moving files'
    )

    return parser.parse_args()
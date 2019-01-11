import argparse
from random_username.generate import generate_username


def main():
    parser = argparse.ArgumentParser(description='Generate Compelling Usernames.')
    parser.add_argument('num_results', type=int, default=1, nargs='?',
                        help='Number of results to return')
    args = parser.parse_args()

    for username in generate_username(num_results=args.num_results):
        print(username)


if __name__ == "__main__":
    main()
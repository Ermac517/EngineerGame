"""Simple CLI to call solver utilities.

Usage examples:
python -m engineergame.cli prime 17
python -m engineergame.cli factorial 6
python -m engineergame.cli fib 10
python -m engineergame.cli gcd 48 18
"""
import argparse
import sys

from . import is_prime, factorial, fibonacci, gcd


def main(argv=None):
    parser = argparse.ArgumentParser(prog="engineergame")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_prime = sub.add_parser("prime", help="Test if a number is prime")
    p_prime.add_argument("n", type=int)

    p_fact = sub.add_parser("factorial", help="Compute factorial")
    p_fact.add_argument("n", type=int)

    p_fib = sub.add_parser("fib", help="Compute nth Fibonacci (0-indexed)")
    p_fib.add_argument("n", type=int)

    p_gcd = sub.add_parser("gcd", help="Compute GCD of two integers")
    p_gcd.add_argument("a", type=int)
    p_gcd.add_argument("b", type=int)

    args = parser.parse_args(argv)

    if args.cmd == "prime":
        print(is_prime(args.n))
    elif args.cmd == "factorial":
        print(factorial(args.n))
    elif args.cmd == "fib":
        print(fibonacci(args.n))
    elif args.cmd == "gcd":
        print(gcd(args.a, args.b))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

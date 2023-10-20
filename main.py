import yz674.my_package
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="IDS706 Mini Project 7")
    subparsers = parser.add_subparsers(dest="operation")
    
    add_parser = subparsers.add_parser("add", help="add operation")
    add_parser.add_argument("arg1", type=int, help="arg1 of add operation")
    add_parser.add_argument("arg2", type=int, help="arg2 of add operation")
    
    args = parser.parse_args()
    
    yz674.my_package.test(args.arg1, args.arg2)
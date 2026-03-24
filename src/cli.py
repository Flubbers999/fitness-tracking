import argparse


def start_cli(argc, argv: list[str]):
    parser = argparse.ArgumentParser(
        prog="FitNessTracka", description="a CLI for a fitness tracking database"
    )
    parser.add_argument("show")
    parser.add_argument("add")
    parser.add_argument("-j", "--json")
    parser.add_argument("-t", "--text")

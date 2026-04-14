import argparse


def start_cli():
    parser = argparse.ArgumentParser(
        prog="FitNessTracka", description="a CLI for a fitness tracking database"
    )

    # parser.add_argument("query", help="")
    formats = ["Text", "Json"]
    group = parser.add_mutually_exclusive_group()
    get_requests = ["get_user_info"]
    group.add_argument(
        "-g",
        "--get",
        choices=get_requests,
        help="gets specific data from query",
    )
    add_requests = ["bilbiblyb"]
    group.add_argument(
        "-a", "--add", choices=add_requests, help="adds specific data to the database"
    )
    parser.add_argument(
        "-i",
        "--informat",
        choices=formats,
        nargs=1,
        help="Set the input format to json",
    )
    parser.add_argument(
        "-o", "--outformat", choices=formats, help="Set the output format to text"
    )
    parser.add_argument("Query_Args", nargs="*", help="arguments for the query")

    # action="store_true",  # store true means that the arg is stored as a binary value
    parser.parse_args()


if __name__ == "__main__":
    start_cli()

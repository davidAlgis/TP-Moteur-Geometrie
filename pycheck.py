"""
Check folders for flake8 warnings.

This script takes one or more folder paths as input via the -i/--input option,
runs flake8 on each folder with a specific configuration, and prints a success message
if no warnings are found. If warnings exist, it prints the number of warnings along with their details.

The imposed configuration is:
    max-line-length = 79
    extend-select = B950
    extend-ignore = E203,E501,E701.
"""

import argparse
import subprocess
import sys

# Define the flake8 configuration options to be passed as command-line arguments.
flake8_args = [
    "--max-line-length=79",
    "--extend-select=B950",
    "--extend-ignore=E203,E501,E701",
]


def check_folder(folder):
    """
    Check a folder for flake8 warnings with the imposed configuration.

    Runs flake8 on the specified folder using the custom configuration. If no warnings are found,
    prints a success message. Otherwise, prints the number of warnings and their details.

    Parameters:
        folder (str): The path to the folder to check.

    Raises:
        SystemExit: If flake8 is not installed or cannot be found.
    """
    try:
        # Run flake8 on the folder with the specified configuration and capture the output.
        result = subprocess.run(
            ["flake8"] + flake8_args + [folder], capture_output=True, text=True
        )
    except FileNotFoundError:
        print("Error: flake8 is not installed or not found in PATH.")
        sys.exit(1)

    output = result.stdout.strip()

    if not output:
        print(f"[SUCCESS] {folder}: No warnings found.")
    else:
        warnings = output.splitlines()
        num_warnings = len(warnings)
        print(f"[WARNING] {folder}: {num_warnings} warning(s) found:")
        for line in warnings:
            print(line)


def main():
    """
    Parse command-line arguments and check each input folder for flake8 warnings.

    The script expects one or more folder paths to be provided with the -i/--input argument.
    """
    parser = argparse.ArgumentParser(
        description="Check folders for flake8 warnings with a custom configuration."
    )
    parser.add_argument(
        "-i",
        "--input",
        nargs="+",
        required=True,
        help="Input folder(s) to check",
    )
    args = parser.parse_args()

    for folder in args.input:
        check_folder(folder)


if __name__ == "__main__":
    main()

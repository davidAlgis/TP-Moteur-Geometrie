"""
Check folders for flake8 warnings.

This script takes one or more folder paths as input via the -i/--input option,
runs flake8 on each folder with a specific configuration, and prints a success
message if no warnings are found. If warnings exist, it prints the number of
warnings along with their details.
The imposed configuration is:
    max-line-length = 79
    extend-select = B950, D (checks for docstring warnings)
    extend-ignore = E203,E501,E701
"""

import argparse
import subprocess
import sys

# Définition des options de configuration de flake8, incluant la vérification
# des docstrings (via l'extension flake8-docstrings qui produit des codes
# Dxxx).
flake8_args = [
    "--max-line-length=79",
    "--extend-select=B950,D",
    "--extend-ignore=E203,E501,E701",
]


def check_folder(folder):
    """
    Check a folder for flake8 warnings with the imposed configuration including docstring checks.

    Runs flake8 on the specified folder using the custom configuration.
    If no warnings are found, prints a success message.
    Otherwise, prints the number of warnings and their details.

    Parameters:
        folder (str): The path to the folder to check.

    Returns:
        int: The number of warnings found in the folder.
    """
    try:
        # Exécution de flake8 sur le dossier spécifié en passant les arguments
        # définis.
        result = subprocess.run(
            ["flake8"] + flake8_args + [folder],
            capture_output=True,
            text=True,
            check=False,  # On ne lève pas d'exception sur code retour non zéro
        )
    except FileNotFoundError:
        print("Error: flake8 is not installed or not found in PATH.")
        sys.exit(1)

    output = result.stdout.strip()

    if not output:
        print(f"[SUCCESS] {folder}: No warnings found.")
        return 0
    else:
        warnings = output.splitlines()
        num_warnings = len(warnings)
        print(f"[WARNING] {folder}: {num_warnings} warning(s) found:")
        for line in warnings:
            print(line)
        return num_warnings


def main():
    """
    Parse command-line arguments and check each input folder for flake8
warnings including docstring validations.
    The script expects one or more folder paths to be provided with the
    -i/--input argument. At the end, it exits with status 0 if no warnings were
    found or 1 otherwise.
    """
    parser = argparse.ArgumentParser(
        description="Check folders for flake8 warnings with a custom"
        "configuration including docstring checks."
    )
    parser.add_argument(
        "-i",
        "--input",
        nargs="+",
        required=True,
        help="Input folder(s) to check",
    )
    args = parser.parse_args()

    total_warnings = 0
    for folder in args.input:
        total_warnings += check_folder(folder)

    if total_warnings > 0:
        print(f"\nTotal warnings found: {total_warnings}")
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
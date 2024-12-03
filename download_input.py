"""Download input for one Advent of Code puzzle if possible

Uses https://pypi.org/project/advent-of-code-data/ if it's available.
Otherwise, does nothing.
"""

# Standard library imports
import pathlib
import sys

# Third party imports
try:
    from aocd.models import Puzzle
except ImportError:
    pypi_url = "https://pypi.org/project/advent-of-code-data/"
    print(f"Install {pypi_url} to autodownload input files")
    raise SystemExit()


def download(year, day):
    """Get input and write it to input.txt inside the puzzle folder"""
    puzzle = Puzzle(year=year, day=day)

    # Create puzzle directory
    year_path = pathlib.Path(__file__).parent / str(year)
    day_path = year_path / f"{day:02d}_{puzzle.title.replace(' ', '_').lower()}"
    day_path.mkdir(parents=True, exist_ok=True)

    # Download input
    input_path = day_path / "input.txt"
    input_path.write_text(puzzle.input_data)

    # Download example data
    for example in puzzle.examples[:1]:
        example_path = day_path / "example.txt"
        example_path.write_text(example.input_data)

    # Add README with link to puzzle text
    readme_path = day_path / "README.md"
    readme_path.write_text(
        f"# {puzzle.title}\n\n"
        f"**Advent of Code: Day {day}, {year}**\n\n"
        f"See {puzzle.url}\n"
    )

    # Load and create the code.py template
    template_path = pathlib.Path(__file__).parent / "template_code.py"
    if not template_path.exists():
        raise FileNotFoundError(f"Template file '{template_path}' not found!")

    code_path = day_path / "code.py"
    if code_path.exists():
        # Skip to avoid over writing existing code.py
        return
    code_content = template_path.read_text()
    code_content = code_content.replace("{DAY}", str(day)).replace("{YEAR}", str(year))

    code_path.write_text(code_content)


if __name__ == "__main__":
    try:
        # Read year and day from command line
        download(year=int(sys.argv[1]), day=int(sys.argv[2]))
    except Exception as err:
        # Catch exceptions so that Copier doesn't clean up directories
        print(f"Download of input failed: {err}")
        raise SystemExit()

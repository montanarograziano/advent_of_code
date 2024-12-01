# Advent Of Code Solutions
My Advent Of Code solutions written in Python, using a script to download puzzles and input (inspired from [gahjelle/advent_of_code](https://github.com/gahjelle/advent_of_code)).

# Setup the script
This script uses the package `advent-of-code-data` to download puzzle's data. This requires you having set the environment variable `AOC_SESSION`.

You can export it in your current shell, or save it in the folder `~/.config/aocd/token`. See [here](https://github.com/wimglenn/advent-of-code-data/#quickstart) for more info.

## Download dependencies
This project uses `uv` as dependency and python's version manager. Read the [official guide](https://docs.astral.sh/uv/getting-started/installation/) to set it up.

Once you have `uv` setup, simply run `uv sync` to download all project dependencies (_advent-of-code-data_ and _ruff_).

# Running the script
Once you have all set up, run `download_puzzles.sh` passing the *YEAR* parameter to download all puzzles for that year.

For example, to download puzzles for year 2023:

```
./download_puzzles.sh 2023
```

The script will create a folder _2023_ and a subfolder or each day, from 1 to 25, filling them with a _code.py_ file that you can fill with your solution, an _example1.py_ and _input.txt_ with the puzzle's input, and a _README.md_ with a link to the puzzle.

I recommend creating alias to run the code with either the complete input or the small example. For example:

```alias aot="uv run python code.py example.txt"```

```alias aoc="uv run python code.py input.txt"```
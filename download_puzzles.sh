#!/bin/bash
# Check if the year is provided as an argument
set -e
if [ -z "$1" ]; then
    echo "You need to provide an year. Usage: $0 <year>"
    exit 1
fi


YEAR=$1
SCRIPT_DIR=$(pwd)
PYTHON_SCRIPT="$SCRIPT_DIR/download_input.py"

# Verify the Python script exists
if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "Error: Python script 'download_input.py' not found in $SCRIPT_DIR"
    exit 1
fi

# Loop through days 1 to 25
for DAY in {01..25}; do
    echo "Setting up Day $DAY for Year $YEAR..."

    # Call the Python script with the current year and day
    python "$PYTHON_SCRIPT" "$YEAR" "$DAY"

    # Check if the Python script executed successfully
    if [ $? -ne 0 ]; then
        echo "Error setting up Day $DAY. Exiting."
        exit 1
    fi
done

echo "Setup complete for Year $YEAR!"

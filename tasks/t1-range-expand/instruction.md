# Range Expander

Write a program that expands a compact list of number ranges into the full,
sorted list of integers.

## Interface

Create your program at `/app/solution.py`. It will be run like this:

    python3 /app/solution.py "<ranges>"

The ranges string is passed as a single command-line argument. Your program
must print the expanded list to standard output.

## Input format

The input is a comma-separated list of tokens. Each token is one of:

- a single non-negative integer, for example `5`
- a range `A-B` (A and B non-negative integers, A <= B), meaning every integer
  from A to B inclusive, for example `2-4` means 2, 3, 4

There may be extra spaces around commas and tokens. Treat them as insignificant.

## Output format

Print the integers on a single line, separated by single spaces, followed by a
newline. The output must be:

- sorted in ascending numeric order (not string order)
- deduplicated (each integer appears at most once), even when ranges overlap

If the input is empty or contains only whitespace, print an empty line.

## Example

Input:

    python3 /app/solution.py "1-3,5"

Output:

    1 2 3 5

Your program will be graded on a variety of inputs, not just this example.

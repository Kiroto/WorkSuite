# Arabic Numerals to Roman Numerals
This python script takes in a number input in arabic numerals (0-9) and outputs it as a number in roman numerals (I-M) via the console.
## Installation Steps
You need to be able to execute python files with python 3. On that note, the methods of obtaining python to run the program differ from system to system. Here's the specifics on Windows and most Linux distributions.
### Windows
1. Go to [the official python website](https://www.python.org/downloads/), download and install the latest python 3 version.
2. Clone this repository locally.
3. Execute the `main.py` file with python.
### Linux
1. Open your terminal.
2. Run the command `sudo apt-get install python3` (You will need administrator privileges). This will install Python 3 on your computer.
3. Clone this repository where suitable and navigate to it.
4. Execute `python3 main.py` on your terminal.

## Requirements
### Functional Requirements
* Transforms non-rational numbers written in arabic numerals to roman numerals.
* Supports numbers from 1 to any positive number.
    * Use big numbers at your own risk
### Non-Functional Requirements
* Mis-input handling
* Allows multiple inputs per run
* Practical
## Acceptance Criteria
* The user can an input arabic numerals and the program shows roman numerals corresponding to the input.
    * Or an error if the arabic numeral is negative, rational, or 0.
## Test Cases
### Unit Tests
<!-- TODO: What is the output for all outputs (does it crash? what does it return?)-->
* The transformative function should reject non-numbers.
* The transformative function should reject decimal or otherwise rational numbers.
* The transformative function should reject 0 or lower numbers.
* The transformative function correctly transforms the following test numbers:
    * 1 (I)
    * 4 (IV)
    * 40 (XL)
    * 39 (XXXIX)
    * 69 (LXIX)
    * 4000 (IV with a line above)
    * 4000000 (MMMM with a line above)
### End-To-End
Each test documented here comes from the initial state (start) of the program.
*To Input* data is to type the requested information into the console after the question prompt, and finally pressing the `Enter` key.
The question form has `Write the number to be transformed to a roman numeral.` as a header.
<!-- TODO: Add prerequisites, test IDs, and descriptions; make it a table? -->
* Inputting `39.5` returns an error message; program doesn't crash.
* Inputting `-8` returns an error message; program doesn't crash.
* Inputting `0` returns an error message; program doesn't crash.
* Inputting `-72.5` returns an error message; program doesn't crash.
* Inputting `39` returns `XXXIX` on the next line.
* Inputting `4000000` returns `MMMM` with a line above on the next line.
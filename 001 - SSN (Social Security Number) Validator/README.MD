# Arabic do Numerals
This python script takes in a text input and validates that it is a well formed and valid SSN number
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
## Instruction Manual
This program has a user manual with instructions on how to properly use the script.
Refer to the [user manual](docs/MANUAL.MD).

## Requirements
### Functional Requirements
* The valid SSN (Social Security Number) must satisfy the following conditions:
    * It should have 9 digits.
* It should be divided into 3 parts by hyphen (-).
    * The first part should have 3 digits and should not be 000, 666, or between 900 and 999.
    * The second part should have 2 digits and it should be from 01 to 99.
    * The third part should have 4 digits and it should be from 0001 to 9999.

### Non-Functional Requirements
* Allows multiple inputs per run
* Practical
* [ ] Automated tests.
* Documentation
    * [x] Installation instructions
    * [x] User Manual
    * [ ] Test Cases
        * [ ] Positive Scenarios
        * [ ] Negative Scenarios
## Acceptance Criteria
* [ ] For a text input, the program's user must know whether or not the text input is a valid SSN.

## Test Cases
This program has a bunch of test case documentation in it's respective [test documentation file](docs/TESTCASES.MD).
The unit tests are written in python and reside in it's [own file](./ssnValidatorTest.py).
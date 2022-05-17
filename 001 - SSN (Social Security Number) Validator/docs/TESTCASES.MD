# Test Cases
These are the test cases for the SSN Validator script.
Unit tests are for specific core functions, and end to end tests are for the program running in the console.
## Unit Tests
These tests are to be ran by the [automated test file](../ssnValidatorTest.py).
The script will end on an exception if the tests fail.
### Positive Cases
* `checkSsn` should return `True` for the following inputs
    * `111-11-1111`
    * `123-45-6789`
    * `899-99-9999`
    * `555-47-7789`
### Negative Cases
* `checkSsn` should return `False` for the following inputs
    * `999-99-9999`
    * `000-55-5555`
    * `555-55-0000`
    * `555-00-5555`
    * `666-66-6666`
    * `987-65-4321`
    * `Teen Wolf`
    * `123456789`
    * `111-111-111`
    * `1-1-1`
    * `1111-1111-1111`
    * `555/47/7789`
## End to End Tests
These tests are to be ran manually by a user.
### Positive Cases
* Typing the following in the console will announce to the user that the codes are valid
    * `111-11-1111`
    * `123-45-6789`
    * `899-99-9999`
    * `555-47-7789`
### Negative Cases
* Typing the following into the console will announce to the user that the codes are invalid
    * `999-99-9999`
    * `000-55-5555`
    * `555-55-0000`
    * `555-00-5555`
    * `666-66-6666`
    * `987-65-4321`
    * `Teen Wolf`
    * `123456789`
    * `111-111-111`
    * `1-1-1`
    * `1111-1111-1111`
    * `555/47/7789`
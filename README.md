# Assignment

**Question 1:**

You must first write black box tests aimed at testing functions relevant to the Moderator program. The test suite file is called test.py and can be found in the 'Test Suite' slide.

There are two functions which must be tested: is_valid_name() and is_chronological(). The test suite program will be run against various implementations of the functions: one correct implementation and many incorrect implementations. This is to ensure your test suite can catch a wide range of bugs. You are not required to implement the functions, just to write tests.

The test suite program must print two lines to the terminal in the following format: <function_name> has <pass_status>. If the function being tested failed one or more of your tests, the test suite should print <function_name> has failed. once only. If the function being tested passes all tests, the test suite should print <function_name> has passed. once only.

Ensure you are testing the functions, not implementing them.

is_valid_name(name: str) -> bool 

is_valid_name() accepts one positional argument name and returns a boolean. The function returns True if the name is valid and False if the name is invalid - validation rules can be found under the 'Validation Rules' section. The function returns False if name is not a string.

is_chronological(earlier_dt: str, later_dt: str) -> bool 

is_chronological() accepts two positional arguments earlier_dt and later_dt and returns a boolean. The function returns True if later_dt represents a datetime that is chronologically later then earlier_dt, and False otherwise. The function returns False if either argument is not a string, or if the strings provided are not in the correct datetime string format.

validation rules for Q1:

Names:
A name is permitted to contain the following:
- English characters A-Z, upper or lower case
- Space character
- 'Minus'/'dash' symbol: -

A name is invalid if it:
- Contains a character not in the above list
- Consists only of space characters
- Has no characters (is empty)

Datetime strings:
Whenever a datetime is represented as a string, it will be in the following format:

YYYY-MM-DDTHH:NN:SS 

where YYYY is the year, MM is the month, DD is the day, T is the literal character 'T', HH is the hour, NN is the minute, and SS is the second. The length of the format is fixed for all values, such that if the month is January, it will be represented as 01. YYYY, MM, DD, HH, NN, and SS must be digits. 
You may assume that if the above format is matched, the datetime string represents a valid datetime.

An example: 1996-09-12T16:30:16

Anything that deviates from this format is considered an invalid datetime string.

**Question 2:**

The Moderator program requires the following command line arguments:

**-task** <task> where <task> is one of the following: rank_people, validate_forum, censor_forum, evaluate_forum 
  
**-log** <filename> where <filename> is the name of the file where the log should be written
  
**-forum** <filename> where <filename> is the name of the file containing the forum messages
  
**-words** <filename> where <filename> is the name of the file containing banned words
  
**-people** <filename> where <filename> is the name of the file containing forum users' names and personality scores

All arguments must be provided. If an argument is not provided, the program should print** No <arg> arguments provided**. and stop immediately, where <arg> (without the -) is the first argument in the list above that is missing.
If the <task> argument does not match a value in the options list, the program should print Task argument is invalid. and stop immediately.
**The arguments can be provided in any order.**

If any of the <filename> arguments for -forum, -words, or -people refers to a file that does not exist (or the program cannot read for any reason) the program should print <filename> cannot be read. for the first <filename> that is not readable (in the above order) and then stop immediately. As an example: if provided -forum bad.forum and -words bad.words where both files are unreadable, the program should print bad.forum cannot be read. 

If multiple errors in the program call are incorrect, the first error that applies from above should be printed.
If the program call is correct, the program should print "Moderator program starting.."

RISTRICTIONS
  
- for keyword
- in keyword
- lambda keyword
- any() function
- all() function
- filter() function
- map() function
- eval() function
- global keyword
- import keyword. Allowed import statements:
     import math
     import datetime
     import sys 
     any module you have written, e.g. import moderator

- A submission containing a file longer than 3000 lines or larger than 500kB will not be accepted. To check the file sizes of your files, use the bash command ls -s --block-size=KB
  
SAMPLE ARGUMENT

python3 moderator.py -task censor_forum -log example.log -forum example.forum -words example.words -people example.people
  
  => should print "Moderator program starting.." in terminal
  

** Question 3:**
  
The Moderator program must validate and interpret a people file listing users of a forum. It should extract personality scores and then rank users according to their score, writing this ranking back to the file in descending order.

An example use of the program for this part is as follows:

$ python3 moderator.py -task rank_people -log example.log -forum example.forum -words example.words -people ./example/example.people
In the above example, the people file is specified as ./example/example.people

The file will contain a comma separated list of names and personality scores. The format of the file is as follows:

The file header (format specified in the 'Validation rules' section)
All subsequent lines are people entries.
People entries:

Each people entry will be structured like so: <name>,<score>\n
The <name> and <score> validity is detailed in the 'Validation rules' section under 'Names' and 'Personality score' respectively.

The program must first check that each line of the file is of the correct format. 
If the file header is not in the correct format, the program should write the following to the log file: Error: people file read. The people file header is incorrectly formatted 
If a people entry is not structured in the format <name>,<score>\n, the program should write the following to the log file: Error: people file read. The people entry is invalid on line <x> where <x> is the line number (the first line of the file is line 1).
If a name is invalid, the program should write the following to the log file: Error: people file read. The user's name is invalid on line <x> where <x> is the line number.
If a personality score is invalid, the program should write the following to the log file: Error: people file read. The personality score is invalid on line <x> where <x> is the line number.

If an error in formatting is encountered, the program should write to the log as specified above, and then exit immediately - the people file should not be modified. If multiple errors are present in the file, the error on the earliest line should be logged, i.e. an error on line 3 is reported if both line 3 and 4 contain errors.
If the file format is valid, nothing should be written to the log but the log file should still be created (yet empty).

Once the file has been validated, the program must read the personality scores, rank the people and then rewrite the file (with the same name) in descending order of personality score rank. If two people share the same personality score, their order from the original file should be kept.
  
validation rules:

A personality score must be a whole number between -10 and 10 (inclusive). 

File headers:
Files for forums, people, and words all start with a file header. A file header is structured as follows:
The first line of the file is the forum title. The forum title can contain any text (including whitespace) but may not be empty.
The second line of the file is a blank line.

# Assignment

Question:

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

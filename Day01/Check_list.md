## About
### Introduction
The methodology of School 21 makes sense only if peer-to-peer reviews are done seriously. Please read all guidelines carefully before starting the review.
- Please, stay courteous, polite, respectful and constructive in all communications during this review.
- Highlight possible malfunctions of the work done by the person and take the time to discuss and debate it.
- Keep in mind that sometimes there can be differences in interpretation of the tasks and the scope of features. Please, stay open-minded to the vision of the other.
- If you have not finished the project yet, it is compulsory to read the entire instruction before starting the review.

### Guidelines
- Evaluate only the files that are in src folder on the GIT repository of the student or group.
- Ensure to start reviewing a group project only when the team is present in full.
- Use special flags in the checklist to report, for example, an “empty work” if repository does not contain the work of the student (or group) in the src folder of the develop branch, or “cheat” in case of cheating or if the student (or group) are unable to explain their work at any time during review as well as if one of the points below is not met. However, except for cheating cases, you are encouraged to continue reviewing the project to identify the problems that caused the situation in order to avoid them at the next review.
- Doublecheck that the GIT repository is the one corresponding to the student or the group.
- Meticulously check that nothing malicious has been used to mislead you.
- In controversial cases, remember that the checklist determines only the general order of the check. The final decision on project evaluation remains with the reviewer.

## MAIN PART
### Exercise 00 - Functional Purse
- Check that the script includes three required functions - `add_ingot(purse)`, `get_ingot(purse)` and `empty(purse)`
- Check that an object passed as an argument is never being modified directly, and a new object is created instead. This includes direct assignments to dictionary keys (cases like `=`, `+=` or `-=` are considered direct assignments)
- Check that `add_ingot(purse)` function increases the number of gold ingots in a purse by one, e.g. `add_ingot({"gold_ingots": 6})` returns `{"gold_ingots": 7}`
- Check that `get_ingot(purse)` function decreases the number of gold ingots in a purse by one, e.g. `get_ingot({"gold_ingots": 6})` returns `{"gold_ingots": 5}`
- Check that `empty(purse)` returns an empty dictionary
- Check that `add_ingot(get_ingot(add_ingot(empty(purse))))` returns `{"gold_ingots": 1}`.
- Check that all three functions work with empty dictionary as an input without any errors
- Check that all three functions work with dictionary containing something different from "gold_ingots" as an input without any errors

### Exercise 01 - Splitwise
- Check that the program includes a function `split_booty`
- Check that the function can accept one, two or more arguments by using star notation
- Check that function returns three empty purses if no gold ingots are in input
- Check that for any given combination of purses and quantity of ingots the total number of them in any two of three returned purses the difference between the numbers of ingots is no larger than 1
- Check that no direct assignments to dictionary keys are used in `split_booty` function (cases like `=`, `+=` or `-=` are concidered direct assignments)

### Exercise 02 - Burglar Alarm
- Check that whenever functions `add_ingot(purse)`, `get_ingot(purse)` or `empty(purse)` are called, a word "SQUEAK" is printed
- Check that function code isn't modified for this particular task in any way, and instead a decorator is used

## BONUS PART
### Testing
- Check that additional tests are implemented as a separate code for checking the business logic of the solutions

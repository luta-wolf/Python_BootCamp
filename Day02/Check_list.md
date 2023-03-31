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
### Exercise 00 - Gaining Access
- Check that the program includes a class `Key`
- Check that `len()` given an instance of `Key` returns 1337
- Check that `key[404]` (if `key` is an instance of Key) gives 3
- Check that `key > 9000` (if `key` is an instance of Key) returns True
- Check that `key.passphrase` (if `key` is an instance of Key) returns "zax2rulez"
- Check that `str()` given an instance of `Key` returns "GeneralTsoKeycard"
- Check that no containers (lists, dicts, sets etc.) are created inside class' methods

### Exercise 01 - Morality
- Check that the program includes classes `Game`, `Player`, `Cheater`, `Cooperative`, `Copycat`, `Grudger` and `Detective`
- Check that classes `Cheater`, `Cooperator`, `Copycat`, `Grudger` and `Detective` are subclasses of `Player`
- Check that by default code simulates 10 matches between two players on each call to `play()` function
- Check that method `top3()` prints current top three player's behaviors along with their current score
- Check that by default `play()` is called for every pair of instances from 5 different types of behavior, resulting into 10 rounds by 10 matches
- Check that by default the winners printed are ``` copycat 57 grudger 46 cheater 45 ``` (the variant where number three is `detective 45` is also considered correct)

## BONUS PART
### Bonus section for EX00
- Check that a complete list of tests for cases mentioned in task is included in solution and key passes all of them

### Bonus section for EX01 - Custom case
- Check that a custom behavior type (class) is present in code (also inherited from `Player`)

### Bonus section for EX01 - Good behavior
- Check that a custom behavior class instance performs better in "contest between each pair of players" (with 5 default ones present) than at least three other behavior types

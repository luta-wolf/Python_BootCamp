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
Exercise 00 - Energy Flow
- Check that "energy.py" is present
- Check that "energy.py" includes function called `fix_wiring()`
- Check that `fix_wiring()` connects everything correctly with plugs when iterators have the same number of elements
- Check that `fix_wiring()` doesn't generate connections including extra cables when `cables` iterator contains more elements than `sockets`
- Check that `fix_wiring()` doesn't generate connections including extra cables when  `sockets` iterator contains more elements than `cables`
- Check that `fix_wiring()` does generate connections "welding" cables to sockets when there is not enough plugs
- Check that `fix_wiring()` filters out any non-string values from input iterators

### Exercise 01 - Personalities
- Check that file 'personality.py' is present
- Check that file 'personality.py' contains a generator (function with `yield` statement) called `turrets_generator()`
- Check that `Turret` class is not declared explicitly and dynamic generation with `type` is used instead
- Check that methods `shoot()`, `search()` and `talk()` of generated turrets are printing "Shooting", "Searching" and "Talking", correspondently
- Check that personality trait values are sampled randomly from range `[0, 100]`
- Check that for every turret the sum of personality trait values is equal to 100

### Exercise 02 - Backpressure
- Check that "pressure.py" script is present
- Check that "pressure.py" contains two generator functions - `emit_gel()` and `valve()`
- Check that function `emit_gel()` accepts an integer argument called `step`
- Check that `emit_gel()` cannot generate values above 100 or below 0
- Check that `emit_gel()` samples the actual step value from the range `[0, step]`
- Check that `valve()` uses send to flip the sign on `step` value inside the `emit_gel()` generator when it emits values >= 80 and < 90
- Check that `valve()` uses send to flip the sign on `step` value inside the `emit_gel()` generator when it emits values < 20 and >= 10
- Check that `valve()` uses closes the `emit_gel()` generator when it emits values >= 90 and <= 100
- Check that `valve()` uses closes the `emit_gel()` generator when it emits values < 10 and >= 0

## BONUS PART
### Bonus section for EX00
- Check that the body of `fix_wiring()` can be represented as one line and doesn't contain block-starting colons

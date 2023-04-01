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

##  MAIN PART
### Exercise 00 - Innocent Prank
- Check that "exploit.py" is present
- Check that "evilcorp_hacked.html" is generated on script run
- Check that the `<title>` tag in a generated file now contains text "Evil Corp - Stealing your money every day"
- Check that the script properly parses name and pronoun from HTML file (especially if they are replaced with different ones of different length)
- Check that `<h1>` tag with pronoun, name and "you are hacked" text is injected inside the `<body>` tag
- Check that Trenton's script from the task is injected into a body of a page
- Check that the word "hacked" appears as an alert if you open the generated file in a browser and submit data through form
- Check that the link at the bottom of the page now leads to "https://mrrobot.fandom.com/wiki/Fsociety"
- Check that the name of the company at the bottom is now replaced with "Fsociety"

### Exercise 01 - Cash Flow
Check that "producer.py" and "consumer.py" scripts are present
Check that producer generates messages and sends them to Redis pubsub queue
Check that produced messages are following the structure mentioned in the task (with "metadata", including both "from" and "to", and "amount")
Check that generated account numbers consist of exactly 10 digits
Check that consumer accepts list of "bad guys" via `-e` command line parameter, separated by comma
Check that consumer reads messages from the Redis pubsub queue
Check that consumer works even without `-e` specified (not modifying input stream) or with just one "bad guy"
Check that the transaction is not modified by consumer if "amount" is negative
Check that sender and receiver ("from" and "to") are switched if receiver is in the list of "bad guys"
Check that the transaction is not modified by consumer if "from" is a "bad guy" while "to" isn't

###  Exercise 02 - Deploy
- Check that "gen_ansible.py" script is present
- Check that "deploy.yml" file is generated on script run
- Check that "deploy.yml" file includes task(s) for packages installation (from "todo.yml") in Ansible notation (regardless of target OS)
- Check that "deploy.yml" file includes task(s) for copying over all files (from "todo.yml") in Ansible notation
- Check that "deploy.yml" file includes task(s) for running exploit and consumer in Ansible notation
- Check that task for running consumer also includes "bad guys" from "todo.yml"


## BONUS PART
### Bonus section for EX01
- Check that producer allows to log all generated messages using builtin `logging` module


### Bonus section for EX02
- Check that a generated "deploy.yml" is actually runnable by Ansible and produces expected result (you may use a virtual machine for that or just builtin Ansible unit test wrappers)

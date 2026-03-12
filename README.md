# python-algorithm-practice-with-tests


# Run ALL tests

RUN TEST FILE

python3 -m unittest test_problems.py

Run ONE specific test class

python3 -m unittest test_problems.TestStreakProblems


Run ONE specific test

python3 -m unittest test_problems.TestStreakProblems.test_longest_heads_basic

These all involve loops + validation + retry behaviour.

Question 3A — retry_password(password)

A computer login requires a password.

The function should keep asking until the correct password is entered.

Correct password: "admin123"

Behavior:

Wrong password → print "Access Denied"

Correct password → print "Login Successful" and stop

Question 3B — guess_number()

A game asks the player to guess a secret number.

Secret number: 7

Behavior:

If the guess is wrong → print "Wrong guess"

If correct → print "Correct!" and stop

Question 3C — retry_code(code)

A door lock requires a 3-digit security code.

Correct code: 999

Behavior:

Wrong code → print "Invalid Code"

Correct code → print "Door Unlocked" and stop

Question 3D — atm_attempt(pin)

An ATM allows unlimited attempts until the correct PIN is entered.

Correct PIN: 4321

Behavior:

Wrong → "Wrong PIN"

Correct → "Welcome!"

Question 3E — unlock_phone(pin)

A phone requires the correct PIN.

Correct PIN: 0000

Behavior:

Wrong → "Try again"

Correct → "Phone Unlocked"


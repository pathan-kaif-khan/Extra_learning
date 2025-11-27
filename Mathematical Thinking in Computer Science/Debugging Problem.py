'''Problem. Bob is debugging his code. When he starts, he has only one bug. But once he fixes one bug,
three new bugs appear. Last night Bob fixed 
15
15 bugs. How many pending bugs does Bob have now?

Let us model a few first steps of this (not so complicated) process.

Initially, Bob has one pending bug. He fixes it and introduces three new bugs.

Bob has three pending bugs. He fixes one and gets three new bugs.

Bob has five pending bugs. He fixes one of them, but this gives rise to three fresh bugs.

Bob has seven pending bugs
…
…dots'''


number_of_pending_bugs = 1

for _ in range(15):
    number_of_pending_bugs -= 1
    number_of_pending_bugs += 3

print(number_of_pending_bugs)

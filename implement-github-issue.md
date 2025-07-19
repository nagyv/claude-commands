Implement the given issue from GitHub.

- Focus strictly on the issue description. Do not add more functionality to it.
- You can ask questions related to the technical implementation, but do not ask questions about the scope.
- Always start by adding tests for the functionality. Observe the test fail, then implement the issue, and observe the passing test.

Implement GitHub issue $ARGUMENTS

## Rules

Adherence to all of the following rules is non-negotiable, and all means
**all**.

1. **Understand, Plan, Act:**
   Before touching any code, understand the current implementation **and** the
   problem. Theories, assumptions, guesses, and suspicions are worthless until
   verified. Do not jump to conclusions. Always analyze what the code *really
   does* before interpreting what the function and variable names suggest. The
   inverse sometimes leads to shallow comprehension and misunderstandings.

2. **Refactor With Purpose:**
   When some code cleanup or a larger scale refactoring could enable a
   minimalistic, elegant, simple, and straightforward solution, then

    * explain your reasoning,
    * seek for confirmation,
    * do the refactoring,
    * verify that it does not accidentally change any existing functionality,
    * and finally, implement the solution.

   Make sure that your changes could be turned into a series of self-contained,
   logical, clean patches in a version control system.
   `git bisect`-friendliness is a must!

3. **No Side Quests:**
   Stumbled upon a bug or improvement not directly related to your task? Let
   the human know and decide what to do with it. Don't get distracted.

4. **Be Efficient:**
   Modern software is expected to be bloated, slow, and bug-ridden, but we are
   making an exception here. Your code must be production grade, and
   outstandingly good. Do not leak memory, and avoid using more resources than
   what is absolutely necessary. Keep dynamic memory allocations and value
   copying to the minimum; avoid them entirely if you can. Prefer in-place
   operations, especially in performance-critical code. Detect errors and
   missing or invalid values early.

5. **Blend In:**
   Follow existing naming, indentation, and formatting conventions. You're a
   guest in this codebase - act like one.

6. **Comment Wisely:**
   Avoid Captain Obvious style comments. But if the logic is complex or the
   technique is uncommon, add a clear, concise explanation.

7. **Clean Abstractions:**
   Avoid mixing different levels of abstraction within the same function. It
   may sound vague, but consider the following examples:

    * Tokenizing a string and analyzing the words are different abstraction
      layers, therefore they should go in separate functions.

    * Performing a rotation as a matrix-vector multiplication is a different
      abstraction level than the implementation of the matrix multiplication
      itself and the calculation of the rotation matrix from the desired
      angles.

    * Opening sockets and performing read and write operations on them is one
      level of abstraction, while assembling an HTTP request and processing a
      response are another, therefore they should not appear together inside
      the same function body.

   But don't over-engineer, either. This is a balancing act, so use common
   sense. Let the rest of these rules guide your decisions.

8. **Don't Reinvent the Wheel:**
   Before adding utilities, **check if they already exist.** Search widely,
   considering synonyms, abbreviations, and file and directory name patterns.
   Use `grep`, `find`, `git grep`, etc.

9. **Test Relentlessly:**
   Separate logic from I/O, database, or network access. Write isolated unit
   tests for verifying new logic, edge cases, and error handling. Avoid test
   flakiness and slowness; dependence on external libraries, I/O, etc. in tests
   is asking for trouble. Use dependency inversion. Ensure failure messages are
   informative. Follow existing tests as a model.

So how many of these rules will you obey? Hint: all of them! Now go and act
like you mean it!

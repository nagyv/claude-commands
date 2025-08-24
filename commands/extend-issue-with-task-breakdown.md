Read issue $ARGUMENTS, and EXTEND the description with a detailed implementation plan that could be handled over to a junior developer. 

The implementation plan should have the issue broken down into small deliverable pieces (called tasks) that each can be reviewed and merged separately within one day of work.

## Task breakdown

1. First set up all the places where modifications are planned using comments and code skeletons. The goal is to
   - give an overview to the user in the PR of the expected modifications
   - avoid merge conflicts due to multiple tasks touching the same codebase
   - always study the current directory structure before coming up with paths and behavior for new files
2. Handle code updates in tasks, focusing on meaningful but small sets of changes that are easy to review
   - code updates should be accompanied by related, extensive unit tests
   - each task should focus on a few codepath changes set up for them with comments and code skeletons
   - a small change can be reviewed in <1 hour by a senior engineer
3. As a final task or tasks, add feature level "functionality", like
   - update localisation files
   - implement feature-level tests (implementation or BDD tests)
   - etc
4. Do not introduce new functionality beyond what is already described in the issue; try to minimize the scope of work!

## Git strategy for the tasks

- The detailed implementation plan should specify the main work branch of work, e.g. `issue-109`
- Every task should work on its dedicated branch, e.g. `issue-109-task-1`
- There should be one PR to merge the main work branch to the default branch
- There should be one PR per task to merge the task branch to the main work branch

## Example content

<example-content>
## Detailed Implementation Plan

**Main work branch**: `issue-109`

- After task 0, all subsequent tasks should branch of off the main work branch
- After task 0, all subsequent tasks should open PRs to the main work branch

This issue is broken down into X small deliverable pieces that can each be reviewed and merged separately within one day of work:

### Task 0: Create the skeleton changes

**Branch**: `issue-109`
**Estimated Time**: 1-2 hours

- Create the main work branch
- Create a skeleton for every new class, method, function call needed for the implementation
   - Add a comment describing the object's intent
   - Mark the comment as `TODO for task X` where X is the task number to write the body of the object

   <example-new-object>
   function calculateRectangleArea(length: number, width: number) -> number:
       // TODO for task 3: This function calculates the area of a rectangle
       return 1
   end function
   </example-new-object>

- Add a TODO comment (`TODO for task X`) to every class, method, function call that needs to be modified with details about the needed modification.
   <example-comment>
   // TODO for task 1: refactor to use the new get_admin_user
   </example-comment>
- Do NOT write any tests at this stage

#### Files to create/modify:

- create skeleton for
  - `get_admin_user` in `src/auth.py`
  - ...
- mark `Auth::is_admin` for refactor to use the `get_admin_user` method
- ...

#### Deliverables:

- New skeleton files created
- `TODO for task X` comments added everywhere needed
- Opened PR and pushed changes
  - The PR description describes the intended flow of information between the changed objects
  - Sequence and Flow diagrams are encouraged to explain how the various components will work together to provide the functionality
 
### Task 1: Admin Role Authorization Foundation

**Branch**: `issue-109-task-1-admin-auth`
**Estimated Time**: 4-6 hours

**Objective**: ...

#### Objects to create/modify:

Needs to fix every `TODO for task 1` prefixed codebase. This might include new objects or refactorings.

- write `get_admin_user`
- call the new `get_admin_user` from the `Auth::is_admin` method
- ...

#### Deliverables:

- Create get_admin_user() function that:
   - Validates JWT token format and expiration
   - Extracts app_metadata.role from JWT payload
   - Returns user info if role is "admin", raises 403 otherwise
- Add comprehensive unit tests covering:
   - Valid admin tokens
   - Missing/invalid tokens
   - ...

#### Success Criteria:

- Tests pass with >95% coverage
- Admin auth utilities are ready for reuse
- No breaking changes to existing code
- No more `TODO for task 1` prefixed comments found in the codebase

### Task 2: ...

</example-content>

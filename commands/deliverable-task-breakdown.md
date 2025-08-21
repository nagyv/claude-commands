Read issue $ARGUMENTS, and EXTEND the description with a detailed implementation plan that could be handled over to a junior developer. 

The implementation plan should have the issue broken down into small deliverable pieces (called tasks) that each can be reviewed and merged separately within one day of work.

## Git strategy for the tasks

- The detailed implementation plan should specify the main work branch of work, e.g. issue-109
- Every task should work on its dedicated branch, e.g. issue-109-task-1
- When a task depends on a previous task, its branch should be based off of the previous task
- There should be one PR to merge the main work branch to the default branch
- There should be one PR per task to merge the task branch to its target branch

<example content>
## Detailed Implementation Plan

**Main branch**: issue-109

This issue is broken down into X small deliverable pieces that can each be reviewed and merged separately within one day of work:

### Task 0: Set up and push main branch

- All subsequent tasks should branch of off the main branch
- All subsequent tasks should open PRs to the main branch

### Task 1: Admin Role Authorization Foundation

**Branch**: issue-109-task-1-admin-auth
**Estimated Time**: 4-6 hours

**Objective**: ...

#### Files to create/modify:

- `path/to/file.ext` - Short description of modifications
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

### Task 2: ...

</example content>

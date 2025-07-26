Create a detailed, step-by-step task list in Markdown format based on an existing Product Requirements Document (PRD) in GitHub issue $ARGUMENTS. The task list should guide a developer through implementation.

## Output

- **Format:** Markdown (`.md`)
- **Location:** New GitHub issues added as sub-issues to the initial PRD issue; use the `--project <project number>` flag to add the issues to the same project as $ARGUMENTS

**Hint:** Get the PRD issue ID and related project number using:

```
# Get GraphQL IDs  
gh api graphql -f query='{
  repository(owner: <owner>, name: <repo name>) {
    issue(number: <issue number>) {
      id,
      projectItems(first: 10) {
        nodes {
          id
          project {
            id
            number
          }
        }
      }
    }
  }
}'
```

## Process

1.  **Receive PRD Reference:** The user points the AI to a specific PRD issue
2.  **Analyze PRD:** The AI reads and analyzes the functional requirements, user stories, milestones, and other sections of the specified PRD.
3.  **Phase 1: Generate Parent Tasks:** Based on the PRD analysis, create the issues and generate the main, high-level tasks required to implement the feature. Use your judgement on how many high-level tasks to use informed by the milestones from the PRD. It's likely to be about 3-7. Present these tasks to the user in the specified format (without sub-tasks yet). Inform the user: "I have generated the high-level tasks based on the PRD. Ready to generate the sub-tasks? Respond with 'Go' to proceed."
4.  **Wait for Confirmation:** Pause and wait for the user to respond with "Go".
5.  **Phase 2: Generate Sub-Tasks:** Once the user confirms, break down each parent task into smaller, actionable sub-tasks necessary to complete the parent task. Ensure sub-tasks logically follow from the parent task and cover the implementation details implied by the PRD.
6.  **Identify Relevant Files:** Based on the tasks and PRD, identify potential files that will need to be created or modified. List these under the `Relevant Files` section, including corresponding test files if applicable.
7.  **Generate Final Output:** Combine the parent tasks, sub-tasks, relevant files, and notes into the final Markdown structure.
8.  **Save Task List:** Save the generated tasks as new GitHub issues. Make sure that the tasks are assigned the same project that the PRD issue belongs to.
9.  **Add tasks as sub-issues** Mark the generated issues as being sub-issues of $ARGUMENTS. Use the following calls replacing the arguments as needed:
   ```
   # Get Child issue GraphQL IDs  
   gh api graphql -f query='{
     repository(owner: <owner>, name: <repo name>) {
       issue(number: <issue number>) {
         id
       }
     }
   }'

   # Add sub-issue relationship
   gh api graphql -f query='
   mutation { addSubIssue(input: {
     issueId: "<PRD issue graphql ID>"
     subIssueId: "<Sub issue graphql ID>"
   }) { issue { id, url } subIssue { id, url } }}'
   ```

## Output Format

The generated task list _must_ follow this structure:

```markdown
## Goal

Brief description of the parent task

## Relevant Files

- `path/to/potential/file1.ts` - Brief description of why this file is relevant (e.g., Contains the main component for this feature).
- `path/to/file1.test.ts` - Unit tests for `file1.ts`.
- `path/to/another/file.tsx` - Brief description (e.g., API route handler for data submission).
- `path/to/another/file.test.tsx` - Unit tests for `another/file.tsx`.
- `lib/utils/helpers.ts` - Brief description (e.g., Utility functions needed for calculations).
- `lib/utils/helpers.test.ts` - Unit tests for `helpers.ts`.

### Notes

- Unit tests should typically be placed alongside the code files they are testing (e.g., `MyComponent.tsx` and `MyComponent.test.tsx` in the same directory).
- Use `npx jest [optional/path/to/test/file]` to run tests. Running without a path executes all tests found by the Jest configuration.

## Tasks

- [ ] 1.0 Task Title
  - [ ] 1.1 [Sub-task description 1.1]
  - [ ] 1.2 [Sub-task description 1.2]
- [ ] 2.0 Task Title
  - [ ] 2.1 [Sub-task description 2.1]
- [ ] 3.0 Task Title (may not require sub-tasks if purely structural or configuration)
```

## Interaction Model

The process explicitly requires a pause after generating parent tasks to get user confirmation ("Go") before proceeding to generate the detailed sub-tasks. This ensures the high-level plan aligns with user expectations before diving into details.

## Target Audience

Assume the primary reader of the task list is a **junior developer** who will implement the feature.

<!-- Originally from https://github.com/snarktank/ai-dev-tasks - Apache 2.0 license -->

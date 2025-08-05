Break down GitHub issue $ARGUMENTS by milestones into individual subtask issues (epics), creating sub-issue relationships and connecting them to the same project.

The main issue already contains milestones or clear phases that can be broken down into separate sub-epics to be refined further.

## Output

- **Format:** Markdown (`.md`)
- **Location:** New GitHub issues added as sub-issues to the initial PRD issue; use the `--project <project title>` flag to add the issues to the same project as $ARGUMENTS

**Hint:** Get the PRD issue ID and related project title using:

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
            title
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
2. **Fetch Issue Content:** Read the GitHub issue content to understand milestones and requirements
3. **Identify Milestones:** Parse the issue content to identify distinct milestones or phases
4. **Create Subtask Issues:** For each milestone, create a new GitHub issue with:
   - Clear milestone-focused title
   - Detailed description of what needs to be accomplished in that milestone
5. **Establish Sub-Issue Relationships:** Link each created issue as a sub-issue to the parent:
   ```bash
   # Get child issue GraphQL ID
   gh api graphql -f query='{
     repository(owner: "nagyv", name: "team-grocery-spend") {
       issue(number: <child_issue_number>) {
         id
       }
     }
   }'
   
   # Add sub-issue relationship
   gh api graphql -f query='
   mutation { addSubIssue(input: {
     issueId: "<parent_issue_graphql_id>"
     subIssueId: "<child_issue_graphql_id>"
   }) { issue { id, url } subIssue { id, url } }}'
   ```
6. **Add to Project:** Ensure all created issues are added to the same project as the parent issue using the `--project` flag

## Issue Creation Template

Each milestone issue should follow this structure:

```markdown
# Milestone: [Milestone Name]

**Parent Issue:** Related to #<parent_issue_number>

## Goal

Brief description of what this milestone accomplishes in the overall feature.

## Requirements

- [ ] Requirement 1 from the milestone
- [ ] Requirement 2 from the milestone
- [ ] Requirement 3 from the milestone

## Acceptance Criteria

- [ ] Specific testable criteria 1
- [ ] Specific testable criteria 2
- [ ] Specific testable criteria 3

## Services impacted

[List all the services in the project that need to be worked on, and what needs to be implemented where]

## Implementation Notes

[Any technical considerations, architectural decisions, or implementation hints specific to this milestone]
```

## Example Usage

Input: `issue #50`

Expected behavior:
1. Reads GitHub issue #50
2. Identifies 4 milestones in the issue description
3. Creates 4 new GitHub issues (e.g., #51, #52, #53, #54)
4. Links issues #51-54 as sub-issues of #50
5. Assigns all issues to the same project as issue #50
6. Provides summary of created issues with their relationships

## Error Handling

- Handle cases where no clear milestones are identified: ask the user for a breakdown

## Target Audience

This command is designed for project managers and lead developers who need to break down large feature requests into manageable implementation phases for their development team.

# PR Review Command Factory

Automatically generate a comprehensive PR review command for a specific GitHub issue.

## Usage
```bash
/pr-review:factory <ISSUE_NUMBER>
```

This command will:
1. Read the GitHub issue details and task breakdown
2. Analyze the technical implementation requirements
3. Generate a complete PR review command file at `.claude/commands/pr-review/issue-$ARGUMENTS.md`

## Workflow

### 1. Issue Analysis
- PRIMARILY RELY on the existing context to understand:
  - Technology stack and framework
  - Task breakdown and branch structure  
  - PR numbers and branch names
  - Implementation approach and patterns
 - Secondarily use the original issue $ARGUMENTS, including its comments to get the necessary information

### 2. Technical Context Identification
Use the `general-purpose` agent to analyze the context and determine:
- **Framework/Language**: React Native, Python FastAPI, etc.
- **Key Technologies**: Expo Router, SQLAlchemy, i18next, etc.
- **Testing Framework**: Jest + React Testing Library, pytest, etc.
- **Architecture Patterns**: Component structure, API patterns, etc.
- **Environment Setup**: Virtual environments, package managers, etc.

### 3. Task Structure Parsing
From the context, extract:
- Number of tasks and their descriptions
- Branch naming pattern (e.g., `issue-$ARGUMENTS-task-1`)
- PR numbers for each task
- Sequential dependencies between tasks

### 4. Command File Generation
Use the `general-purpose` agent to create a comprehensive command file that includes:

**IMPORTANT**: When generating the command file, replace all instances of `<DOLLAR_ARGUMENTS>` with a dollar sign followed by ARGUMENTS

This ensures the generated command will properly use Claude Code's argument substitution system.

**Required Sections:**
- **Context**: Issue summary and task breakdown with branch/PR mapping
- **Technical Implementation Details**: Framework-specific architecture and patterns
- **Key Code Patterns**: Language/framework-specific code examples
- **Workflow**: 9-step process from PR analysis to final validation
- **Environment Setup**: Tool-specific commands and directory structure
- **Important Constraints**: Scope limitations and quality requirements

**Technology-Specific Adaptations:**
- Include platform specific tool usage and considerations
- Framework-appropriate testing commands and coverage requirements

### 5. File Creation
Write the generated command to:
```
.claude/commands/pr-review/issue-$ARGUMENTS.md
```

### 6. Validation
Ensure the generated command includes:
- Complete workflow with all 9 steps
- Proper use of `<DOLLAR_ARGUMENTS>` for PR number input (replace <DOLLAR_ARGUMENTS> with the dollar sign followed by ARGUMENTS)
- Technology-specific testing and quality check commands
- Branch mapping for all tasks identified in the issue
- Environment setup instructions
- Agent recommendations (react-native-architect, python-backend-architect, etc.)

## Example Generated Command Structure

The factory will generate commands similar to existing patterns:

```markdown
# PR Feedback Resolution for Issue #$ARGUMENTS

## Context
- Task breakdown with branch and PR mapping

## Technical Implementation Details  
- Framework-specific architecture
- Key technologies and patterns

## Workflow
1. PR Analysis - `gh pr view <DOLLAR_ARGUMENTS>`
2. Branch Setup - checkout appropriate task branch  
3. Feedback Analysis - use appropriate agent
4. Implementation - use appropriate agent
5. Testing & Validation - run framework tests
6. Code Quality Checks - linting, typing, etc.
7. Additional Steps - localization, etc. (if needed)
8. Git Operations - commit and push
9. Final Validation - verify all requirements met

## Environment Setup
- Tool-specific commands and setup

## Example Usage
/pr-review:issue-$ARGUMENTS <PR_NUMBER>

This will:
1. Read feedback from PR <PR_NUMBER> 
2. Switch to the PR's branch  
3. Use the appropriate agent to address the feedback
4. Run all relevant tests and linting to ensure they pass
5. Update assets if needed
6. Commit and push the changes
```

## Success Criteria
The generated command file should:
- Be immediately usable without manual editing
- Include all necessary technical context
- Have appropriate agent recommendations  
- Include complete testing and quality validation
- Follow the established 9-step workflow pattern
- Be specific to the issue's technology stack and requirements

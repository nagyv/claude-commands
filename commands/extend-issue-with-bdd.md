Use the bdd-test-engineer agent, and extend the issue description of $ARGUMENTS with gherkin-style test requirements. 
Add the BDD test scenarios to the end of the issue description.

<example-output>
## BDD Test Scenarios

### Feature: <short description of the issue, like a title>

```gherkin
**Background:**
  Given ...
  And ...
  And ...
```

#### Scenario: <title of the scenario 1>

```gherkin
  Given ..
  When ...
  Then ...
  And ...
```

#### Scenario: <title of scenario 2>

```gherkin
  Given ..
  When ...
  Then ...
  And ...
```

...
</example-output>

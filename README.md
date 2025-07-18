# Automation tooling
Testing automation tooling for changelogs and release notes.

## Release notes schema

Current schema being tested:

```yaml
# Human-readable name of the charm
charm_name: ""

# Condition for release (revision number, date, etc.)
release_condition: ""

# Details about the change in this artifact
change:
  - author: "" # GitHub profile name
    title: "" # What goes into the header. Should be short (TBD)
    type: "" # major, minor, deprecated, bugfix, breaking
    description: "" # Brief description of the chage or fix.
    url: "" # Link to PR or commit
```
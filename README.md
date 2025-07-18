# Automation tooling
Testing automation tooling for changelogs and release notes.

## Release notes schema

Current schema being tested:

```yaml
# Human-readable name of the charm
charm_name: ""

# Human-readable condition for release (revision number, date, etc.)
release_condition: ""

# Machine-friendly identifier to distinguish individual release notes
release_tag: ""

# Details about the change in this artifact
changes:
  - title: "" # What goes into the header. Should be short (TBD)
    author: "" # GitHub profile name
    type: "" # major, minor, deprecated, bugfix, breaking
    description: "" # Brief description of the chage or fix.
    url: "" # Link to PR or commit
```
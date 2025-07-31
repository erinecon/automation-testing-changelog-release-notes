# Automation tooling
Testing automation tooling for changelogs and release notes.

## Release notes schema -- split artifact approach

`common.yaml`:
```yaml
# Human-readable name of the charm
charm_name: ""

# Human-readable condition for the release (revision number, date, etc.)
release_condition: ""
```

Individual artifact:
```yaml
# Version of the artifact schema
version_schema: 1

# The key holding the change
change:
  - title: "" # What goes into the header. Should be short (TBD)
    author: "" # GitHub profile name
    type: "" # major, minor, deprecated, bugfix, breaking
    description: "" # Brief description of the chage or fix.
    urls: # Relevant URLs
      pr: "" # mandatory link to PR
      related_doc: "" # optional link to related documentation
      related_issue: "" # optional link to related issue
    visibility: public # determines whether artifact should be rendered. Accepted values: public, internal, hidden
    highlight: false # boolean to determine if change is highlight material (i.e. should be featureed in initial paragraph)
```

## Release notes schema -- combined artifact approach

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

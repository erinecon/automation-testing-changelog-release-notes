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
# The key holding the change
change:
  - release_tag: "" # Machine-friendly identifier to distinguish individual release notes
    title: "" # What goes into the header. Should be short (TBD)
    author: "" # GitHub profile name
    type: "" # major, minor, deprecated, bugfix, breaking
    description: "" # Brief description of the chage or fix.
    urls: # Relevant URLs
      - pr: "" # mandatory link to PR
        related_doc: "" # optional link to related documentation
        related_issue: "" # optional link to related issue
    internal: false # boolean to determine if change is internal
    highlight_material: false # boolean to determine if change is highlight material (i.e. should be featureed in initial paragraph)
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
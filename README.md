# Automation tooling
Testing automation tooling for changelogs and release notes.

## Release notes -- split artifact approach

Run:
```
python3 build_release_notes.py
```

Currently hardcoded aspects to keep in mind:

* `artifact_dir`: the directory where your artifacts live.
* `output_dir`: the directory where the rendered output will live.
* `release_tag`: determines the name of the output file like `release-notes-<release_tag>.md`. To be removed or refactored in the future.
* `common_file`: defines the `common.yaml` file. Assumed to live in the same directory as the Python script.
* The Jinja template is assumed to live in a `templates` directory with the name `release-template.md.j2`. 

### Schemas

`common.yaml`:
```yaml
# Human-readable name of the charm
charm_name: ""

# Human-readable condition for the release (revision number, date, etc.)
release_condition: ""

# Boolean to determine whether internal changes will be rendered
show_internal: false
```

Individual artifacts must have names with the format `pr####.yaml`, where
the number represents the pull request associated with the artifact.

Individual "change" artifact schema:
```yaml
# Version of the artifact schema
version_schema: 1

# The key holding the change(s)
changes:
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

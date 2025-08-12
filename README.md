# Automation tooling
Testing automation tooling for changelogs and release notes.

## Release notes -- split artifact approach

Run:
```
python3 build_release_notes.py
```

Usage and options:

```
usage: build_release_notes.py [-h] [-a ARTIFACTDIR] [-o OUTPUTDIR] [-r RELEASEDIR] [-c COMMONFILE] [-t TEMPLATEDIR] [-f TEMPLATEFILE]

Generates release notes based on multiple artifacts

options:
  -h, --help            show this help message and exit
  -a ARTIFACTDIR, --artifactdir ARTIFACTDIR
                        the directory where your change artifacts live
  -o OUTPUTDIR, --outputdir OUTPUTDIR
                        the directory where the rendered output will live
  -r RELEASEDIR, --releasedir RELEASEDIR
                        the directory where your release artifacts live
  -c COMMONFILE, --commonfile COMMONFILE
                        full path to your common.yaml file
  -t TEMPLATEDIR, --templatedir TEMPLATEDIR
                        directory where your release notes template lives
  -f TEMPLATEFILE, --templatefile TEMPLATEFILE
                        name of release notes template file
```

All arguments have default settings:
* `--artifactdir`: `artifacts`
* `--outputdir`: `docs/release-notes`
* `--releasedir`: `releases`
* `--commonfile`: `common.yaml`
* `--templatedir`: `template`
* `--templatefile`: `release-template.md.j2`

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

Release artifact schema:

```yaml
# --- Information about release ----

# list of change artifacts included in the release
included_changes:

# earliest revision included in the release
earliest_revision:

# latest revision included in the release
latest_revision:

# earliest date included in the release
earliest_date:

# latest date included in the release 
latest_date:
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

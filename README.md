# Release notes automation

Tooling and workflows designed to automate release notes in a
data-driven process.

## Change and release artifacts

In the multi-artifact approach, the process follows these steps:

1. On a PR level, include a "change artifact" in a dedicated change artifacts directory to summarize
   the changes to be included in the release.
2. When a release condition is met, add a "release artifact" in a dedicated release artifacts directory.
3. The GitHub Action workflow uses the change artifacts defined in the release artifact to pre-populate
   a Jinja template.
4. The workflow automatically opens a PR to publish the release notes in your repository.
5. Contributors check the release notes, adding more context and information when needed.  
6. Publish the release notes.

### What you'll need

In your repository, you will need the following materials:

* Change artifacts
* Release artifact(s) in a dedicated directory
* Jinja2 template for release notes
* A YAML file with information common to all artifacts (`common.yaml`)

You will also need to call the reusable workflow in your repository:

```yaml
name: 'Create release notes'

on:
  push:
    branches:
      - 'main'
    paths:
      - '<path to your release notes artifacts>'

jobs:
  release-notes:
    uses: canonical/release-notes-automation/.github/workflows/action.yml@main
    secrets: inherit
    with:
      change-artifact-dir: <directory to change artifacts>
      release-output-dir: <directory to release notes>
      release-artifact-dir: <directory to release artifacts>
      common-file: <full path to common.yaml file>
      template-dir: <directory to release notes template>
      template-file-name: <name of release notes template>
```

If you define the workflow like this in your repository, then the workflow
will trigger when you add a new release artifact to your dedicated directory.

### Artifact schemas

Your artifacts can have different schemas depending on your project's needs.
The following examples are based around charms and were created to be used
with the Jinja2 template
[`docs/release-notes/template/release-template.md.j2`](docs/release-notes/template/release-template.md.j2).

Example `common.yaml`:

```yaml
# Human-readable name of the charm
charm_name: ""

# Human-readable condition for the release (revision number, date, etc.)
release_condition: ""

# Boolean to determine whether internal changes will be rendered
show_internal: false
```

Individual change artifacts must have names with the format `pr####.yaml`, where
the number represents the pull request associated with the artifact.

Example of an individual "change" artifact schema:

```yaml
# Version of the artifact schema
version_schema: 1

# The key holding the change(s)
changes:
  - title: "" # What goes into the header. No punctuation please
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

Release artifacts must have names with the format `release####.yaml`, where
the number will be used to tag the output file.

Example release artifact schema:

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

### Python script

You can run the script manually using:
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
                        full path to the YAML file with keys common among all artifacts
  -t TEMPLATEDIR, --templatedir TEMPLATEDIR
                        directory where your release notes template lives
  -f TEMPLATEFILE, --templatefile TEMPLATEFILE
                        name of release notes template file
```

All arguments have default settings:
* `--artifactdir`: `docs/release-notes/artifacts`
* `--outputdir`: `docs/release-notes`
* `--releasedir`: `docs/release-notes/releases`
* `--commonfile`: `docs/release-notes/common.yaml`
* `--templatedir`: `docs/release-notes/template`
* `--templatefile`: `release-template.md.j2`

## Release notes schema -- combined artifact approach

There's also some tooling and materials under the `single-doc` directory
in this repository using a "combined change artifact" approach.

Schema that was being tested:

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

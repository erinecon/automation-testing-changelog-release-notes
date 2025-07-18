import os
import glob
import yaml
from jinja2 import Environment, FileSystemLoader

def main():
    """"Does stuff."""

    # Jinja2 environment 
    env = Environment(loader=FileSystemLoader('template'))
    template = env.get_template('release-template.md.j2')

    artifact_dir = 'test-release'
    output_dir = 'docs/release-notes'

    artifact_files = glob.glob(os.path.join(artifact_dir, '*.yaml'))

    if not artifact_files:
        print("No artifacts found.")
        return
    
    print(f"Found {len(artifact_files)} artifact(s) to process.")

    for artifact in artifact_files:
        print(f"Processing {artifact}...")
        with open(artifact, 'r') as f:
            artifact_data = yaml.safe_load(f)

        # Render template
        content = template.render(artifact_data)

        output_path = os.path.join(output_dir, 'release-notes-test.md')

        with open(output_path, 'w') as f:
            f.write(content)

        print(f"Generated release notes at {output_path}")


if __name__ == '__main__':
    main()
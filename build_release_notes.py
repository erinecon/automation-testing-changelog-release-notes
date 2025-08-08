import os
import glob
import yaml
from jinja2 import Environment, FileSystemLoader

def load_yaml(file_path):
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)
    
def save_yaml(data, file_path):
    with open(file_path, 'w') as f:
        yaml.safe_dump(data, f, default_flow_style=False)

def combine_data(file_paths, output_file):
    combined_data = {}

    for file_path in file_paths:
        data = load_yaml(file_path)
        for key, value in data.items():
            if key in combined_data:
                if isinstance(combined_data[key], list) and isinstance(value, list):
                    combined_data[key].extend(value)
                elif isinstance(combined_data[key], list):
                    combined_data[key].append(value)
                elif isinstance(value, list):
                    combined_data[key] = [combined_data[key]] + value
                else:
                    combined_data[key] = [combined_data[key], value]
            else:
                combined_data[key] = value

    save_yaml(combined_data, output_file)

def main():
    """"Generates release notes based on multiple artifacts."""

    # define variables
    artifact_dir = 'artifacts'
    output_dir = 'docs/release-notes'
    release_dir = 'releases'
    release_tag = '0001'
    combined_file = 'all_data.yaml'
    common_file = 'common.yaml'

    # Jinja2 environment 
    env = Environment(loader=FileSystemLoader('template'))
    template = env.get_template('release-template.md.j2')

    # find artifact files
    artifact_files = glob.glob(os.path.join(artifact_dir, '*.yaml'))

    if not artifact_files:
        print("No artifacts found.")
        return
    
    print(f"Found {len(artifact_files)} artifact(s) to process.")

    # find release artifact
    release_files = glob.glob(os.path.join(release_dir, '*.yaml'))
    release_file = ''
    for rf in release_files:
        # grab release number
        substring = rf[rf.find('.yaml')-4:rf.find('.yaml')]
        # check release tag is equal to substring
        if substring == release_tag:
            release_file = rf

    if not release_file:
        print("No matching release file found.")
        return

    print(f"Found release artifact {release_file} based on tag {release_tag}.")

    release_data = load_yaml(release_file)
    for key, value in release_data.items():
        print("nothing yet")
        # TODO: grab all included changes
    
    # TODO: rename previous artifact_files to all_artifact_files
    # TODO: loop through artifacts and only keep the ones for the release
    # TODO: Something like below except current artifacts use file name (no path)
    '''
    # loop through artifacts
    artifact_files = []
    for artifact in all_artifact_files:
        # grab PR number
        substring = artifact[find('.yaml')-4:artifact.find('.yaml')]
        artifact_num = int(substring)
        if(artifact_num > artifact_cutoff):
            artifact_files.append(artifact)
    '''

    # add release artifact to list of files
    artifact_files.append(release_file)

    # add common file to list of files
    artifact_files.append(common_file)

    # generate combined data
    combine_data(artifact_files, combined_file)
    combined_data = load_yaml(combined_file)

    # render template and save
    content = template.render(combined_data)

    output_filename = "release-notes-" + release_tag + ".md"
    output_path = os.path.join(output_dir, output_filename)

    with open(output_path, 'w') as f:
        f.write(content)

    print(f"Generated release notes at {output_path}")

    # delete file with all artifacts
    os.remove(combined_file)

if __name__ == '__main__':
    main()
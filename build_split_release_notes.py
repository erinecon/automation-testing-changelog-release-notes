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
            print(value)
            if key in combined_data:
                if isinstance(combined_data[key], list):
                    combined_data[key].append(value)
                else:
                    combined_data[key] = [combined_data[key], value]
            else:
                combined_data[key] = value

    save_yaml(combined_data, output_file)

def main():
    """"Generates release notes based on multiple artifacts."""

    # Jinja2 environment 
    env = Environment(loader=FileSystemLoader('template'))
    template = env.get_template('release-split-template-change.md.j2')

    artifact_dir = 'test-split-release'
    output_dir = 'docs/release-notes'
    release_tag = 'rev1-split'
    output_file = 'all_data.yaml'

    artifact_files = glob.glob(os.path.join(artifact_dir, '*.yaml'))

    if not artifact_files:
        print("No artifacts found.")
        return
    
    print(f"Found {len(artifact_files)} artifact(s) to process.")

    # add common file to list of files
    artifact_files.append('common.yaml')

    combine_data(artifact_files, output_file)
    gen = load_yaml(output_file)
    content = template.render(gen)

    ''' 
    all_artifact_data = {}
    all_artifact_data_array = []

    for artifact in artifact_files:
        print(f"Processing {artifact}...")
        with open(artifact, 'r') as f:
            artifact_data = yaml.safe_load(f)
            release_tag_to_compare = artifact_data.get("release_tag")
            # TODO: continue statement if release_tag_to_compare == release_tag
            all_artifact_data.update(artifact_data)
            all_artifact_data_array.append(artifact_data)

    with open('common.yaml', 'r') as f:
        common_data = yaml.safe_load(f)

    # write all data to a single YAML
    with open('all_data.yaml', 'w') as file:
        yaml.dump_all(common_data, file)
        yaml.dump_all(all_artifact_data_array, file) 

    # Render template
    gen = yaml.safe_load('all_data.yaml')

    '''  
    

    # content = template.render(all_artifact_data)

    output_filename = "release-notes-" + release_tag + ".md"
    output_path = os.path.join(output_dir, output_filename)

    with open(output_path, 'w') as f:
        f.write(content)

    print(f"Generated release notes at {output_path}")


if __name__ == '__main__':
    main()
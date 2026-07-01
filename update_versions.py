import argparse
import traceback
import yaml

parser = argparse.ArgumentParser(
    description="A script that modify the image version in dockerhub."
)
parser.add_argument(
    "--commit", type=str, default="fix", help="the type of action in the commit message"
)
args = parser.parse_args()

commit_type = (args.commit).partition(":")[0]
file_path = "docker-compose.yml"

try:
    with open(file_path, "r") as file:
        existing_data = yaml.safe_load(file) or []
except FileNotFoundError:
    existing_data = []

try:
    app_version = (existing_data["services"]["backend"]["build"]["tags"][0]).partition(":")[2]
    app_tag = existing_data["services"]["backend"]["build"]["tags"][0]
    version_table = [int(n) for n in app_version.split(".")]
    if "feat" in commit_type or "test" in commit_type or "build" in commit_type:
        version_table[1] += 1
    else:
        version_table[2] += 1

    new_version = ".".join([str(n) for n in version_table])
    new_app_tag = app_tag.replace(app_version, new_version)
    existing_data["services"]["backend"]["build"]["tags"] = [new_app_tag]

    with open(file_path, "w") as file:
        yaml.dump(existing_data, file, default_flow_style=False, sort_keys=False)
except Exception:
    print("Error")
    traceback.print_exc()
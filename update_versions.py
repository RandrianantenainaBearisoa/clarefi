import argparse
import traceback
import yaml
from enum import Enum

def version_updater(commit_type: str, parts:list[str] = ["backend", "frontend"]):
    file_path = "docker-compose.yml"

    try:
        with open(file_path, "r") as file:
            existing_data = yaml.safe_load(file) or []
    except FileNotFoundError:
        existing_data = []

    try:
        for part in parts:
            app_version = (existing_data["services"][part]["build"]["tags"][0]).partition(":")[2]
            app_tag = existing_data["services"][part]["build"]["tags"][0]
            version_table = [int(n) for n in app_version.split(".")]
            if "feat" in commit_type or "test" in commit_type or "build" in commit_type:
                version_table[1] += 1
            else:
                version_table[2] += 1

            new_version = ".".join([str(n) for n in version_table])
            new_app_tag = app_tag.replace(app_version, new_version)
            existing_data["services"][part]["build"]["tags"] = [new_app_tag]

            with open(file_path, "w") as file:
                yaml.dump(existing_data, file, default_flow_style=False, sort_keys=False)
    except Exception:
        print("Error")
        traceback.print_exc()

parser = argparse.ArgumentParser(
    description="A script that modify the image version in dockerhub."
)
parser.add_argument(
    "--commit", type=str, default="fix", help="the type of action in the commit message"
)

class Part(Enum):
    FRONTEND = "frontend"
    BACKEND = "backend"

    def __str__(self):
        return self.value

parser.add_argument(
    "--part", type=str, default="", help="the part of the compose that is updated: 'frontend' or 'backend' , let empty if both", choices=list(Part)
)
args = parser.parse_args()

if args.part == "frontend":
    version_updater(commit_type=((args.commit).partition(":")[0]), parts=["frontend"])
elif args.part == "backend":
    version_updater(commit_type=((args.commit).partition(":")[0]), parts=["backend"])
else:
    version_updater(commit_type=((args.commit).partition(":")[0]))
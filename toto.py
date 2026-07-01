import argparse

parser = argparse.ArgumentParser(description="A script that modify the image version in dockerhub.")
parser.add_argument("--commit", type=str, default="fix", help="the type of action in the commit message")
args = parser.parse_args()

commit_type = args.commit
print(commit_type)
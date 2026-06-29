from pathlib import Path
import shutil
import traceback

app_path = Path("app")
if app_path.is_dir():
    shutil.rmtree(app_path)
app_path.mkdir(parents=True, exist_ok=True)

directory_list = {
    "config": ["model_config.yaml"],  # copy specific files
    "models/joblibs": [],  # copy all directory content
    "src/api/": [],
    "src/core/inference": [],
    "src/core/utils": [],
}

for directory, files in directory_list.items():
    try:
        source = Path(directory)
        dest = app_path / directory
        if len(files) == 0:
            shutil.copytree(source, dest)
        else:
            dest.mkdir(parents=True, exist_ok=True)
            for file in files:
                shutil.copy2(source / file, dest / file)
    except Exception:
        print(f"\ndirectory : {directory} |", f"files : {files}")
        traceback.print_exc()

import os 

def ensure_dir_exists_by_filename(filename: str) -> None:
    """Ensure that the directory of a file exists."""
    dirname = os.path.dirname(filename)
    if dirname:
        os.makedirs(dirname, exist_ok=True)
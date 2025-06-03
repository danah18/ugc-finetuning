import os

def read_txt_to_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

def create_folders(base_names, root_dir="experts", subfolders=None):
    if subfolders is None:
        subfolders = [
            "downloads",
            "downloads/videos",
            "downloads/transcripts",
            "downloads/transcripts_categorized"
        ]

    for name in base_names:
        for sub in subfolders:
            path = os.path.join(root_dir, name, sub)
            os.makedirs(path, exist_ok=True)

    print(f"Created nested folder structure under '{root_dir}'")

# --- Usage ---
txt_file = "experts/experts.txt" 
names_list = read_txt_to_list(txt_file)
create_folders(names_list)

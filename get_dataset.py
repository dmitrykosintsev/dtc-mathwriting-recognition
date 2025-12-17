from huggingface_hub import snapshot_download

# Download all files into a local folder
snapshot_download(repo_id="deepcopy/MathWriting-human", repo_type="dataset", local_dir="./", allow_patterns="*.parquet")
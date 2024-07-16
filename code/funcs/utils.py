import requests
import tarfile
from tqdm import tqdm
from pathlib import Path


# Configuration
DATA_FILES = [
    {"name": "hcp_rest.tgz", "url": "https://osf.io/bqp7m/download"},
    {"name": "hcp_task.tgz", "url": "https://osf.io/s4h8j/download"},
    {"name": "hcp_covariates.tgz", "url": "https://osf.io/x5p4g/download"},
    {"name": "atlas.npz", "url": "https://osf.io/j5kuc/download"}
]

HCP_DIR = Path('..') / 'data'


def download_file(
        url,
        file_path,
        progress_bar
    ):
    """Download a file from a given URL to a specified path."""
    try:
        r = requests.get(url, stream=True)
        r.raise_for_status()
        
        with file_path.open("wb") as fid:
            for data in r.iter_content(chunk_size=8192):
                size = fid.write(data)
                progress_bar.update(size)
        
        progress_bar.set_description(f"Downloaded {file_path.name}")
        return True
    except requests.RequestException as e:
        progress_bar.set_description(f"Failed to download {file_path.name}: {e}")
        return False


def extract_tgz(
        file_path,
        extract_path,
        progress_bar
    ):
    """Extract a .tgz file to a specified path."""
    try:
        with tarfile.open(file_path, "r:gz") as tar:
            tar.extractall(path=extract_path)
        progress_bar.set_description(f"Extracted {file_path.name}")
        return True
    except tarfile.TarError as e:
        progress_bar.set_description(f"Failed to extract {file_path.name}: {e}")
        return False


def download_and_extract_data(
        data_dir = Path(HCP_DIR),
        files = DATA_FILES,
        force_download = False
    ):
    """
    Download and extract data files to the specified directory.
    
    Args:
    data_dir (Path): The directory to save and extract the data to. Defaults to Path('../data').
    files (list): List of dictionaries containing file information. Defaults to DATA_FILES.
    force_download (bool): If True, re-download files even if they already exist. Defaults to False.
    
    Returns:
    None
    """
    data_dir.mkdir(parents=True, exist_ok=True)

    total_size = sum(int(requests.head(file_info['url']).headers.get('content-length', 0)) for file_info in files)
    
    with tqdm(total=total_size, unit='iB', unit_scale=True, unit_divisor=1024) as progress_bar:
        for file_info in files:
            file_path = data_dir / file_info['name']
            
            if file_path.is_file() and not force_download:
                print(f"Skipping {file_info['name']}: File already exists")
                # Update progress bar to reflect skipped file
                file_size = file_path.stat().st_size
                progress_bar.update(file_size)
            else:
                progress_bar.set_description(f"Downloading {file_info['name']}")
                if download_file(file_info['url'], file_path, progress_bar):
                    if file_path.suffix == '.tgz':
                        progress_bar.set_description(f"Extracting {file_info['name']}")
                        extract_tgz(file_path, data_dir, progress_bar)

    print("All downloads and extractions completed!")

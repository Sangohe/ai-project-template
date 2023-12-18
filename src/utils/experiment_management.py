from typing import List, Union
from pathlib import Path


def find_next_idx(dir_content: List[Path]) -> str:
    """Finds the ID for the next experiment.

    Args:
        dir_content (List[Path]): Files inside directory.

    Returns:
        str: Formatted experiment id.
    """
    if dir_content:
        idxs = [
            int(p.name.split("-")[0][-3:])
            for p in dir_content
            if p.name.split("-")[0][-3:].isnumeric()
        ]
        next_idx = max(idxs) + 1 if idxs else 0
    else:
        next_idx = 0
    return f"{next_idx:03d}"


def create_run_dir(dirname: str, root_dir: str = "results") -> Path:
    """Creates a directory for the current execution"""
    root_path = Path(root_dir)
    if root_path.exists():
        dir_content = [p for p in root_path.iterdir() if p.is_dir()]
        next_idx = find_next_idx(dir_content)
    else:
        next_idx = "000"
    run_dir_path = root_path / f"{next_idx}-{dirname}"
    run_dir_path.mkdir(parents=True, exist_ok=True)
    return run_dir_path


def get_path_of_directory_with_id(
    dir_id: Union[str, int], results_dir: Union[str, Path]
) -> Path:
    if isinstance(dir_id, int):
        dir_id = f"{dir_id:03d}"

    if results_dir == "":
        raise ValueError("`results_dir` cannot be an empty string")

    results_path = Path(results_dir)
    experiment_names = sorted([p.name for p in results_path.iterdir() if p.is_dir()])

    if not experiment_names:
        raise ValueError(f"There are no experiments in {results_dir}")

    experiment_ids = [n.split("-")[0] for n in experiment_names]
    if dir_id not in experiment_ids:
        raise ValueError(f"There is no directory with {dir_id} id")

    idx_of_dir = experiment_ids.index(dir_id)
    experiment_dir_with_id = experiment_names[idx_of_dir]
    return results_path / experiment_dir_with_id

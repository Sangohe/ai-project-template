import argparse
from pathlib import Path

import torch
import wandb

from utils.logging import Logger
from utils.experiment_management import create_run_dir


def train(config=None):
    wandb.init(
        config=config,
        project=config.wandb_project,
        group=config.wandb_group,
        name=config.wandb_name,
    )
    config = wandb.config

    run_dir = create_run_dir("experiment_desc", root_dir=Path().cwd() / "results")
    logs_fname = run_dir / "execution_logs.txt"
    _ = Logger(file_name=str(logs_fname), file_mode="a", should_flush=True)

    # Move model to GPU if available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using {device} device.")

    # Training loop
    for epoch in range(config.epochs):
        wandb.log({"epoch": epoch, "loss": epoch * config.batch_size / 10})
        print(f"Epoch {epoch+1}/{config.epochs}, Loss: {epoch / 10}")

    wandb.finish()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--wandb_project", type=str, default=None)
    parser.add_argument("--wandb_group", type=str, default=None)
    parser.add_argument("--wandb_name", type=str, default=None)
    parser.add_argument("--learning_rate", type=float, default=1e-4)
    parser.add_argument("--epochs", type=int, default=25)
    parser.add_argument("--batch_size", type=int, default=16)
    args = parser.parse_args()

    # Pass the arguments to Wandb
    train(args)

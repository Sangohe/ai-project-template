# Artificial Intelligence Project Template

**Author:** Santiago Gómez, PhD Student

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sangohe)
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://co.linkedin.com/in/santiagogomezh)

This repository serves as a template for deep learning projects, illustrating an organized and scalable project structure and best practices. It's tailored to assist in setting up projects for efficient development and experimentation.

## Suggested Project Structure

```
stroke-segmentation-project/
│
├── src/ # Source code
│ ├── init.py # Makes src a Python module
│ ├── data/ # Data loading and preprocessing
│ ├── models/ # Model architectures
│ ├── utils/ # Utility functions
│ └── train.py # Training script
│
├── tests/ # Test suite
│ ├── test_data.py
│ ├── test_models.py
│ └── ...
│
├── notebooks/ # Jupyter notebooks for experimentation
│ └── ...
│
├── data/ # Data directory (could be symlink if large)
│ ├── train/
│ ├── val/
│ └── test/
│
├── configs/ # Configuration files (e.g., for Wandb)
│ └── ...
│
├── requirements.txt # Project dependencies
├── setup.py # Setup script for packaging
└── README.md # Project documentation
```

### About the src/ layout
- **Organization and Clarity:** The `src/` directory helps in logically organizing your code, separating the source code from datasets, scripts, notebooks, and documentation for better clarity.
- **Modularity:** Encourages a modular design, allowing for a breakdown of the code into different components such as data loading, model architecture, and training routines.
- **Reusability:** Facilitates code reuse across different parts of the project or in other projects.
- **Testing:** Simplifies the setup of testing frameworks and writing tests, targeting specifically the `src/` directory.
- **Packaging and Distribution:** Ideal for packaging the project as a Python package, conforming to common practices.

### Project Examples to Start Developing

- **[src/train.py](./src/train.py)**: This script is the main training pipeline. It initializes Weights & Biases (Wandb) for experiment tracking, sets up logging, and handles the training loop. The training settings, such as the learning rate, batch size, and number of epochs, are configurable through command-line arguments. 

    **Example Command to Run train.py**:
    ```bash
    python src/train.py --wandb_project "MyProject" --wandb_group "ExperimentGroup" --wandb_name "Experiment1" --learning_rate 0.001 --epochs 20 --batch_size 32
    ```

- **[notebooks/template.ipynb](./notebooks/template.ipynb)**: this template serves as a guide for structuring further notebooks, ensuring consistency and clarity in exploratory work and analysis.

- **[configs/sweep_config.yaml](./configs/sweep_config.yaml)**: This configuration file is used to start a hyperparameter sweep with Wandb. It defines a grid search over learning rates and batch sizes, while keeping the number of epochs fixed.

    **Example Command to Start a Wandb Sweep**:
    1. Initialize the sweep:
        ```bash
        wandb sweep configs/sweep_config.yaml
        ```
    2. Start the sweep agent (replace `project` and `sweep_id` with the actual project and ID returned by the previous command):
        ```bash
        wandb agent sangohe/project/sweep_id
        ```

### Learning More about Wandb Tracking and Sweeps

To deepen your understanding of Wandb tracking and sweeps, consider exploring the following resources:

- [Weights & Biases Sweeps Guide](https://docs.wandb.ai/guides/sweeps): This guide provides a comprehensive walkthrough on how to use W&B Sweeps for hyperparameter tuning and experiment tracking, including popular search methods such as Bayesian, grid search, and random.
- [Sweeps Walkthrough](https://docs.wandb.ai/guides/sweeps/walkthrough): This walkthrough outlines the steps to define, initialize, and run a sweep with W&B, covering everything from setting up your training code to visualizing sweep results.

These resources offer detailed insights into how to effectively use Wandb for managing and optimizing your machine learning experiments.

### Environment Setup
Instructions for setting up the environment will be provided once the technologies for the project are decided. This will include steps to install necessary dependencies and how to configure the development environment for optimal performance.

### Considerations
- **Project Size and Scope:** While a `src/` layout might be excessive for smaller projects, it's advantageous for larger, more complex projects, especially with multiple collaborators.
- **Future Expansion:** Anticipating project growth or using it as a foundation for future work warrants starting with a `src/` layout.
- **Learning Curve:** While there might be a learning curve for those new to this structure, it aligns with professional software development practices and is a valuable skill.

Adopting a `src/` layout is highly recommended for projects that are

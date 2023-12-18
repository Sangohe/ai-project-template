# Ischemic Stroke Segmentation

**Author:** Santiago Gómez


## Advantages of src/ Layout
- **Organization and Clarity:** A src/ directory helps in logically organizing your code. It separates the source code from other project files like datasets, scripts, notebooks, documentation, etc., making the project structure clearer and more manageable.
- **Modularity:** It encourages a modular design. You can break down the code into different modules (like data loading, model architecture, training routines), making it easier to maintain and update.
- **Reusability:** With well-organized modules, it's easier to reuse code across different parts of the project or even in other projects.
- **Testing:** A clear separation of source code makes it easier to set up testing frameworks and write tests, as the test suite can specifically target the src/ directory.
- **Packaging and Distribution:** If you plan to package your project as a Python package, a src/ layout is a common practice, making it easier to define the package and its contents.

## Suggested Project Structure

Based on the src/ layout, here's a suggested structure for your PyTorch project:

```
stroke-segmentation-project/
│
├── src/                    # Source code
│   ├── __init__.py         # Makes src a Python module
│   ├── data/               # Data loading and preprocessing
│   ├── models/             # Model architectures
│   ├── utils/              # Utility functions
│   └── train.py            # Training script
│
├── tests/                  # Test suite
│   ├── test_data.py
│   ├── test_models.py
│   └── ...
│
├── notebooks/              # Jupyter notebooks for experimentation
│   └── ...
│
├── data/                   # Data directory (could be symlink if data is large)
│   ├── train/
│   ├── val/
│   └── test/
│
├── configs/                # Configuration files (e.g., for Wandb)
│   └── ...
│
├── requirements.txt        # Project dependencies
├── setup.py                # Setup script for packaging
└── README.md               # Project documentation
```

## Considerations
- **Size and Scope of the Project:** For smaller projects or quick prototypes, a src/ layout might be overkill. However, for larger, more complex projects, especially those involving multiple collaborators, it's beneficial.
- **Future Expansion:** If you anticipate the project will grow or be used as a basis for future work, starting with a src/ layout is a good practice.
- **Learning Curve:** For those new to such structures, there might be a slight learning curve. However, it's a valuable skill, aligning with professional software development practices.

In conclusion, if your project is expected to be medium to large in scale, involves multiple components (like different models, various data processing steps), or you aim for high code quality and reusability, adopting a src/ layout is highly recommended.
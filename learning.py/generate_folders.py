import os
from pathlib import Path

def create_ml_structure(root_drive="I:"):
    """Create the optimized ML/DL file structure on specified drive"""
    
    # Define the complete structure
    structure = {
        "0_SYSTEM": {
            "conda": None,
            "envs": {
                "torch": None,
                "tf": None,
                "light": None
            },
            "temp": None,
            "logs": None
        },
        "1_CODE": {
            "active": {
                "proj1": {
                    "src": None,
                    "notebooks": None,
                    "configs": None
                },
                "proj2": {
                    "src": None,
                    "notebooks": None,
                    "configs": None
                }
            },
            "templates": {
                "pytorch": None,
                "keras": None
            }
        },
        "2_DATA": {
            "00_raw": None,
            "01_interim": None,
            "02_processed": None,
            "03_features": None,
            "04_cache": None
        },
        "3_MODELS": {
            "checkpoints": None,
            "deployed": None,
            "benchmarks": None
        },
        "4_RESOURCES": {
            "@compressed": {
                "videos": None,
                "images": None
            },
            "docs": None
        },
        "5_ARCHIVE": {
            "zipped_projects": None,
            "retired_models": None
        }
    }

    # Create all directories
    base_path = Path(f"{root_drive}/ML_MASTER")
    
    def make_structure(base, structure):
        for name, children in structure.items():
            path = base / name
            path.mkdir(exist_ok=True, parents=True)
            print(f"Created: {path}")
            if children:
                make_structure(path, children)
    
    print(f"\nCreating ML/DL structure on {root_drive} drive...")
    make_structure(base_path, structure)
    print("\nStructure created successfully!")
    
    # Create a README file
    readme = base_path / "README.md"
    readme_content = """# ML_MASTER Directory Structure

This is an optimized structure for machine learning/deep learning projects.

## Space Allocation
- 0_SYSTEM: 6GB (Core software)
- 1_CODE: 15GB (Active projects)
- 2_DATA: 60GB (Data pipeline)
- 3_MODELS: 15GB (Model artifacts)
- 4_RESOURCES: 10GB (Learning materials)
- 5_ARCHIVE: 4GB (Cold storage)
"""
    readme.write_text(readme_content)
    print(f"Created: {readme}")

if __name__ == "__main__":
    create_ml_structure("I:")
    input("Press Enter to exit...")
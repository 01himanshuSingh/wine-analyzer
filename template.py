import argparse
import logging
import os
from pathlib import Path


logging.basicConfig(
    level=logging.INFO,
    format="[ %(asctime)s ] %(message)s",
)


def get_list_of_files(project_name: str) -> list[str]:
    return [
        ".github/workflows/.gitkeep",
        ".gitignore",
        "LICENSE",
        "README.md",
        "requirements.txt",
        "setup.py",
        "pyproject.toml",
        "Dockerfile",
        ".dockerignore",
        "config/config.yaml",
        "params.yaml",
        "schema.yaml",
        "research/trials.ipynb",
        f"src/{project_name}/__init__.py",
        f"src/{project_name}/components/__init__.py",
        f"src/{project_name}/components/data_ingestion.py",
        f"src/{project_name}/components/data_validation.py",
        f"src/{project_name}/components/data_transformation.py",
        f"src/{project_name}/components/model_trainer.py",
        f"src/{project_name}/components/model_evaluation.py",
        f"src/{project_name}/config/__init__.py",
        f"src/{project_name}/config/configuration.py",
        f"src/{project_name}/entity/__init__.py",
        f"src/{project_name}/entity/config_entity.py",
        f"src/{project_name}/pipeline/__init__.py",
        f"src/{project_name}/pipeline/stage_01_data_ingestion.py",
        f"src/{project_name}/pipeline/stage_02_data_validation.py",
        f"src/{project_name}/pipeline/stage_03_data_transformation.py",
        f"src/{project_name}/pipeline/stage_04_model_trainer.py",
        f"src/{project_name}/pipeline/stage_05_model_evaluation.py",
        f"src/{project_name}/utils/__init__.py",
        f"src/{project_name}/utils/common.py",
        f"src/{project_name}/constants/__init__.py",
        f"src/{project_name}/logging/__init__.py",
        "artifacts/data_ingestion/.gitkeep",
        "artifacts/data_validation/.gitkeep",
        "artifacts/data_transformation/.gitkeep",
        "artifacts/model_trainer/.gitkeep",
        "artifacts/model_evaluation/.gitkeep",
        "logs/.gitkeep",
        "templates/index.html",
        "main.py",
        "app.py",
    ]


def create_project_structure(project_name: str, base_dir: str = ".") -> None:
    list_of_files = get_list_of_files(project_name)
    base_path = Path(base_dir)

    for filepath in list_of_files:
        filepath = base_path / filepath
        filedir, filename = os.path.split(filepath)

        if filedir:
            os.makedirs(filedir, exist_ok=True)
            logging.info(
                "Creating directory: %s for the file: %s",
                filedir,
                filename,
            )

        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            with open(filepath, "w"):
                pass

            logging.info("Creating empty file: %s", filepath)
        else:
            logging.info("%s already exists", filename)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Scaffold an end-to-end machine learning project structure."
    )
    parser.add_argument(
        "project_name",
        help="Python package name under src/ (e.g. ml_project)",
    )
    parser.add_argument(
        "--base-dir",
        default=".",
        help="Directory where the project structure should be created.",
    )
    args = parser.parse_args()

    create_project_structure(args.project_name, args.base_dir)


if __name__ == "__main__":
    main()

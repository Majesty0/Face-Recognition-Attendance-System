"""
Training Controller
"""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Allow imports from src
sys.path.append(str(PROJECT_ROOT / "src"))

def train_model():
    """
    Executes the model training.
    """
    try:
        import runpy

        runpy.run_path(
            str(PROJECT_ROOT / "src" / "10_train_custom_model.py"),
            run_name="__main__"
        )

        return True

    except Exception as e:
        print(e)
        return False
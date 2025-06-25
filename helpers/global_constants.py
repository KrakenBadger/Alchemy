from pathlib import Path


__all__ = ["ROOT_DIR", "TEMPLATE_DIR", "STATIC_DIR"]


ROOT_DIR = Path(__file__).parent.parent.resolve()

TEMPLATE_DIR = ROOT_DIR / "templates"
STATIC_DIR = ROOT_DIR / "static"

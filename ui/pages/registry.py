from pathlib import Path
import importlib
import inspect
from typing import Dict, Optional, Type

from ui.pages.page import BasePage

PageClass = Type[BasePage]

_page_registry: Optional[Dict[int, PageClass]] = None

def _pages_root() -> Path:
    return (Path(__file__).resolve().parent / 'presets').resolve()



def _iter_page_modules():
    presets_dir = Path(__file__).resolve().parent / 'presets'

    print("[Registry] Scanning:", presets_dir)

    for path in presets_dir.glob('*.py'):
        if path.name == "__init__.py":
            continue

        mod = f"ui.pages.presets.{path.stem}"
        print("[Registry] --> Found module:", mod)

        yield mod


def build_registry() -> Dict[int, PageClass]:

    registry: Dict[int, PageClass] = {}

    for module_name in _iter_page_modules():
        try:
            module = importlib.import_module(module_name)

        except Exception as exc:
            print(f"[Registry] Failed to import {module_name}: {exc}")
            continue

        for _, obj in inspect.getmembers(module, inspect.isclass):
            if not issubclass(obj, BasePage) or obj is BasePage:
                continue

            page_id = getattr(obj, 'page_id', None)
            if page_id is None:
                continue

            if not isinstance(page_id, int):
                raise TypeError(f"[Registry] {obj.__name__}.page_id must be int, got {type(page_id).__name__}")

            if page_id in registry:
                existing = registry[page_id]
                raise ValueError(
                    f"[Registry] Duplicate page_id {page_id} found in "
                    f"{existing.__module__}.{existing.__name__} and "
                    f"{obj.__module__}.{obj.__name__}"
                )

            registry[page_id] = obj

    return registry


# --- PUBLIC API -------------------------------------------------------------

def get_page_class(page_id: int) -> Optional[PageClass]:

    global _page_registry

    if _page_registry is None:
        _page_registry = build_registry()

    return _page_registry.get(page_id)


def refresh_registry() -> None:

    global _page_registry
    _page_registry = build_registry()
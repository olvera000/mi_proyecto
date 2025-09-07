"""
Entry point for mi_proyecto.

Provides a simple greet function and a CLI.
"""

from __future__ import annotations

import argparse
import sys


def greet(name: str = "Mundo") -> str:
    """Return a friendly greeting.

    Args:
        name: Optional name to include in the greeting.

    Returns:
        A greeting string.
    """

    return f"Hola, {name}!"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Ejemplo de CLI para mi_proyecto")
    parser.add_argument(
        "--name",
        "-n",
        default="Mundo",
        help="Nombre a saludar (por defecto: Mundo)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    print(greet(args.name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

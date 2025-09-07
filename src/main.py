"""
Entry point for mi_proyecto.

Provides a simple greet function and a CLI.
"""

from __future__ import annotations

import argparse
import sys


def greet(name: str = "Mundo", uppercase: bool = False) -> str:
    """Return a friendly greeting.

    Args:
        name: Optional name to include in the greeting.
        uppercase: If True, return the greeting in uppercase.

    Returns:
        A greeting string.
    """

    message = f"Hola, {name}!"
    return message.upper() if uppercase else message


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Ejemplo de CLI para mi_proyecto")
    parser.add_argument(
        "--name",
        "-n",
        default="Mundo",
        help="Nombre a saludar (por defecto: Mundo)",
    )
    parser.add_argument(
        "--uppercase",
        "-U",
        action="store_true",
        help="Imprime el saludo en MAYÚSCULAS",
    )
    parser.add_argument(
        "--times",
        "-t",
        type=int,
        default=1,
        help="Número de repeticiones del saludo (por defecto: 1)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    for _ in range(args.times):
        print(greet(args.name, uppercase=args.uppercase))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

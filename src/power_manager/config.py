"""Configuration helpers for power-manager."""

from __future__ import annotations

import copy
from typing import Any, Optional


DEFAULT_CONFIG = {
    "default_animation": "fire",
    "debug_log": "/tmp/power-manager-debug.log",
}


def config_defaults() -> dict:
    """Return default configuration values."""
    return copy.deepcopy(DEFAULT_CONFIG)


def config_schema() -> dict:
    """Return JSON Schema for configuration."""
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "properties": {
            "default_animation": {
                "type": "string",
                "description": "Default animation to use (fire, fade, sakura, none)",
            },
            "debug_log": {
                "type": "string",
                "description": "Path to debug log file",
            },
        },
        "additionalProperties": False,
    }


def validate_config_file(config_path: Optional[Any] = None) -> list[str]:
    """Validate config file. No config file system — always valid."""
    return []


def load_config() -> dict:
    """Return resolved configuration (defaults only, no config file)."""
    return copy.deepcopy(DEFAULT_CONFIG)

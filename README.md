# Power Manager

Power action orchestrator with visual animation hooks for Wayland compositors.

Coordinates smooth visual transitions with system power actions like shutdown, reboot, and suspend. Uses [shutdown-effect](https://github.com/Ckrest/shutdown-effect)'s hook system to discover and run animations.

## Features

- **Visual Transitions**: Animated overlays for shutdown/reboot/suspend
- **Hook System**: Discovers animations from shutdown-effect (bundled + user-provided)
- **Instant Mode**: `--animation none` for immediate power actions
- **Test Mode**: Preview animations without triggering power actions
- **Suspend Resume**: Automatic cleanup after wake from sleep

## Installation

```bash
git clone https://github.com/Ckrest/power-manager.git
cd power-manager

# Also install shutdown-effect for animations
git clone https://github.com/Ckrest/shutdown-effect.git ../shutdown-effect

# Create symlink (optional)
ln -s $(pwd)/power-manager ~/bin/power-manager
```

### Dependencies

- Python 3.10+
- [shutdown-effect](https://github.com/Ckrest/shutdown-effect) - Animation discovery and bundled animations
- `loginctl` (for logout action)
- `efibootmgr` (for Windows dual-boot)

Optional (for cleanup after test/suspend):
- Wayfire with `screen-freeze` and `cursor-control` plugins

## Usage

```bash
# Shutdown with default animation
power-manager shutdown

# Reboot with fade animation
power-manager reboot --animation fade

# Suspend without animation (instant)
power-manager suspend --animation none

# Test animation without power action
power-manager test --animation sakura

# Show help and available animations
power-manager --help
```

### Animation Discovery

Animations are discovered via shutdown-effect's hook system:

1. `SHUTDOWN_EFFECTS_DIR` environment variable (if set)
2. `~/.config/shutdown-effect/animations/` (user animations)
3. `shutdown-effect/animations/` (bundled defaults)

```bash
# See available animations
power-manager --help

# Add custom animations
mkdir -p ~/.config/shutdown-effect/animations/my-effect
# Create animate.py following shutdown-effect protocol
```

## Architecture

```
┌─────────────┐     ┌────────────────┐     ┌─────────────────┐
│   wlogout   │────▶│ power-manager  │────▶│ shutdown-effect │
│   (UI)      │     │ (orchestrator) │     │  (discovery)    │
└─────────────┘     └───────┬────────┘     └────────┬────────┘
                            │                       │
                            │◀── READY/BLACK ───────┘
                            ▼
                    ┌───────────────┐
                    │   systemctl   │
                    └───────────────┘
```

## Configuration

Set default animation by editing the script:
```python
DEFAULT_ANIMATION = "fire"  # Or any discovered animation name
```

Or use environment variable to override animation directory:
```bash
SHUTDOWN_EFFECTS_DIR=/custom/animations power-manager shutdown
```

## wlogout Integration

Example `~/.config/wlogout/layout`:
```json
{
    "label": "shutdown",
    "action": "/path/to/power-manager shutdown",
    "text": "Shutdown"
}
```

## License

MIT License - see [LICENSE](LICENSE)

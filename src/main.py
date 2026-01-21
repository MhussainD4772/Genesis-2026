"""
Genesis 2026 - Main Entry Point
A modern game development project
"""

import json
import sys
from pathlib import Path


def load_config():
    """Load game configuration from config file"""
    config_path = Path(__file__).parent.parent / "game_config.json"
    with open(config_path, 'r') as f:
        return json.load(f)


def main():
    """Main game entry point"""
    print("=" * 50)
    print("Genesis 2026 - Game Engine Starting")
    print("=" * 50)
    
    # Load configuration
    config = load_config()
    game_info = config.get('game', {})
    
    print(f"\nGame Title: {game_info.get('title')}")
    print(f"Version: {game_info.get('version')}")
    print(f"Description: {game_info.get('description')}")
    
    settings = config.get('settings', {})
    resolution = settings.get('defaultResolution', {})
    print(f"\nResolution: {resolution.get('width')}x{resolution.get('height')}")
    print(f"Target FPS: {settings.get('targetFPS')}")
    
    print("\n✓ Game engine initialized successfully!")
    print("Ready for development...\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame engine shutdown requested.")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)

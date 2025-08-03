#!/usr/bin/env python3
"""
Claude Code Hook: UserPromptSubmit
Saves user prompts to user_prompts.yaml file with timestamps

Example output:

user_prompts:
  "2025-07-30 18:39": |
     Here comes the sun
  "2025-07-30 18:41": |
     Little darling
"""
import os
import sys
import json
from datetime import datetime
import yaml
from pathlib import Path


def main():
    # Read the event data from stdin
    try:
        event_data = json.load(sys.stdin)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON input: {e}", file=sys.stderr)
        sys.exit(1)

    # Extract the user prompt from the event data
    user_prompt = event_data.get('prompt', '')
    if not user_prompt:
        print("No user prompt found in event data", file=sys.stderr)
        sys.exit(1)

    # Generate timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Define the YAML file path
    yaml_file = Path(os.getenv("CLAUDE_PROJECT_DIR"), "user_prompts.yaml")

    # Load existing data or create new structure
    if yaml_file.exists():
        try:
            with open(yaml_file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f) or {}
        except yaml.YAMLError as e:
            print(f"Error reading YAML file: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        data = {}

    # Ensure user_prompts key exists
    if 'user_prompts' not in data:
        data['user_prompts'] = {}

    # Add the new prompt with timestamp
    data['user_prompts'][timestamp] = user_prompt

    # Write back to file
    try:
        with open(yaml_file, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, default_flow_style=False,
                      allow_unicode=True, indent=2, default_style='|')
    except Exception as e:
        print(f"Error writing to YAML file: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

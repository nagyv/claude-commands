# claude-commands
Clone to ~/.claude/commands

```
cd ~
cp .claude .claude.bak
git clone git@github.com:nagyv/claude-commands.git .claude
```

You might want to move back some files and directories from the backed up `.claude.bak` or just `rm -rf .claude.bak`

## Hooks setup

Copy the hook scripts (from `/hooks`) to your `${CLAUDE_PROJECT_DIR}/bin/` folder.

### Requirements

- PyYAML

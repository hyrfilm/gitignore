# gitignore

A simple command-line tool to manage `.gitignore` files from anywhere in your repo.

## Install

```bash
curl -fsSL https://raw.githubusercontent.com/hyrfilm/gitignore/master/gitignore -o ~/.config/gitignore
```

> `~/.local/bin` should already be on your PATH. If not, add this to your `~/.zshrc` or `~/.bashrc`:
> ```bash
> export PATH="$HOME/.local/bin:$PATH"
> ```

## Usage

```bash
gitignore .env .DS_Store       # add one or more patterns
gitignore --defaults           # common patterns (.DS_Store, .env, *.log, .vscode/ ...)
gitignore --python             # Python patterns (__pycache__/, .venv/, .pytest_cache/ ...)
gitignore --js                 # JS/Node patterns (node_modules/, dist/, .next/ ...)
gitignore --list               # show current .gitignore
gitignore --undo coverage      # remove a pattern and untrack matching files
```

Works from any subdirectory — the tool walks up to find the repo root automatically.
Already-tracked files matching a newly added pattern are untracked via `git rm --cached`.

## Update

```bash
curl -fsSL https://raw.githubusercontent.com/hyrfilm/gitignore/master/gitignore -o ~/.config/gitignore/gitignore
```

## Uninstall
```bash
rm ~/.config/gitignore ~/.local/bin/gitignore
```

# gitignore

A simple command-line tool to manage `.gitignore` files from anywhere in your repo.

## Install

```bash
curl -fsSL https://raw.githubusercontent.com/hyrfilm/gitignore/main/gitignore -o ~/.config/gitignore && chmod +x ~/.config/gitignore && ln -sf ~/.config/gitignore ~/.local/bin/gitignore
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
gitignore --elixir             # Elixir/Mix patterns (_build/, deps/, *.beam ...)
gitignore --go                 # Go patterns (*.exe, *.test, go.work ...)
gitignore --ocaml              # OCaml patterns (_build/, _opam/, *.cmi ...)
gitignore --racket             # Racket patterns (compiled/, *.zo, *.rkt~ ...)
gitignore --list               # show current .gitignore
gitignore --undo coverage      # remove a pattern (tracked files are left alone)
```

Works from any subdirectory — the tool walks up to find the repo root automatically.
Already-tracked files matching a newly added pattern are untracked via `git rm --cached`.

## Adding a language

Pattern sets live in `templates/<flag>.gitignore` as ordinary gitignore files, so you can
paste one straight from [github/gitignore](https://github.com/github/gitignore). The first
line is a header, `# Label: help text`, that becomes the section heading and the `--help` text.
Comments and blank lines are ignored.

```bash
cp ~/Downloads/Rust.gitignore templates/rust.gitignore   # add a header line at the top
./build.py                                               # regenerates the table in `gitignore`
```

## Update

```bash
curl -fsSL https://raw.githubusercontent.com/hyrfilm/gitignore/main/gitignore -o ~/.config/gitignore
```

## Uninstall
```bash
rm ~/.config/gitignore ~/.local/bin/gitignore
```

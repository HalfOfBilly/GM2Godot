# Contributing to GM2Godot

First off, thank you for considering contributing to GM2Godot! It's people like you that make GM2Godot such a great tool. We welcome contributions from everyone and are grateful for even the smallest of fixes!

## Table of Contents
1. [Code of Conduct](#code-of-conduct)
2. [Getting Started](#getting-started)
   - [Issues](#issues)
   - [Pull Requests](#pull-requests)
3. [Development Setup](#development-setup)
4. [Coding Standards](#coding-standards)
5. [Commit Messages](#commit-messages)
6. [Testing](#testing)
7. [Documentation](#documentation)
8. [Community](#community)
9. [Other](#other)

## Code of Conduct

This project and everyone participating in it is governed by the [GM2Godot Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to [prayforniceland@gmail.com].

## Getting Started

Contributions to GM2Godot are made via [Issues](https://github.com/Infiland/GM2Godot/issues) and [Pull Requests.](https://github.com/Infiland/GM2Godot/pulls)

- Search for existing Issues and PRs before creating your own.
- We work hard to makes sure issues are handled in a timely manner but, depending on the impact, it could take a while to investigate the root cause. A friendly ping in the comment thread to the submitter or a contributor can help draw attention if your issue is blocking.

### Issues

Issues should be used to report problems with the library, request a new feature, or to discuss potential changes before a PR is created. I am yet to make templates in the future to make this a bit easier.

If you find an Issue that addresses the problem you're having, please add your own reproduction information to the existing issue rather than creating a new one. Adding a [reaction](https://github.blog/2016-03-10-add-reactions-to-pull-requests-issues-and-comments/) can also help be indicating to our maintainers that a particular problem is affecting more than just the reporter.

### Pull Requests

PRs to our libraries are always welcome and can be a quick way to get your fix or improvement slated for the next release. In general, PRs should:

- Only fix/add the functionality in question OR address wide-spread whitespace/style issues, not both.
- Add unit or integration tests for fixed or changed functionality (if a test suite already exists).
- Address a single concern in the least number of changed lines as possible.
- Include documentation in the repo if nessesary.

For changes that address core functionality or would require breaking changes (e.g. a major release), it's best to open an Issue to discuss your proposal first. This is not required but can save time creating and reviewing changes.

In general, we follow the ["fork-and-pull" Git workflow](https://github.com/susam/gitpr)

1. Fork the repository
2. Clone the project to your machine

```
git clone https://github.com/Infiland/GM2Godot
```

3. Create a branch
4. Commit changes to the branch
5. Following any formatting and testing guidelines specific to this repo
6. Push changes to your fork
7. Open a PR in our repository and follow the PR template so that we can efficiently review the changes.

## Development Setup

To set up GM2Godot for development:

1. Fork and clone the repository
```
git clone https://github.com/Infiland/GM2Godot
```
2. [Install Python 3.9.0 or later](https://www.python.org/downloads/)
3. Install required libraries:
   ```
   pip install Pillow markdown2 tkhtmlview
   ```
4. If you're on Linux, install Tkinter:
   ```
   sudo apt-get install python3-tk python3-pil python3-pil.imagetk python3-markdown2
   ```
   (if tkhtmlview is a problem, please use pip install tkhtmlview --break-system-packages)
5. Run the program with:
   ```
   python main.py
   ```

## Project Structure

The project structure will keep changing as more features are added
The main components/important parts of GM2Godot are:

- `main.py`: Main application
- `gui.py`: Handles GUI main elements

- `converter.py`: Handles and runs all of the conversion
- `sprites.py`: Handles sprite conversion
- `sounds.py`: Handles sound conversion
- `fonts.py`: Handles font conversion
- `notes.py`: Handles note conversion
- `tilesets.py`: Handles tileset conversion
- `shaders.py`: Converts GameMaker shaders to GDScript shaders
- `project_settings.py`: Copies GameMaker settings to Godot
- `included_files.py`: Copies GameMaker included files to Godot

### Folders
- `img`: Contains image files
- `src`: Contains main functionality
- `gui`: Has GUI related code

## Coding Standards

While not strict, it's good to follow these: (Even I mess up!)

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code style
- Use meaningful variable and function names
- Write clear comments and docstrings if nessesary
- Keep functions small and focused on a single task

## Commit Messages

While not strict, it's good to follow these: (Even I mess up!)

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Reference issues and pull requests if nessesary

## Testing

Testing would require having both a GameMaker project and a Godot project.

You can snag my GameMaker project from this repo for testing:
```
git clone https://github.com/Infiland/TheColorfulCreature
```
You do not have to have GameMaker or run this project in GameMaker, but if you want to perform testing in Godot, run GM2Godot and use Godot 4.3 to create an empty project.

## Documentation

Documentation is a crucial part of this project. Please make sure to update the documentation when you make changes to the code.
This includes the README.md and CONTRIBUTING.md files

## Community

Discussions about GM2Godot take place on this repository's [Issues](https://github.com/Infiland/GM2Godot/issues) and [Pull Requests](https://github.com/Infiland/GM2Godot/pulls) sections. Anybody is welcome to join these conversations.

Wherever possible, do not take these conversations to private channels, including contacting the maintainers directly. Keeping communication public means everybody can benefit and learn from the conversation.

## Other

GameMaker is developing a new runtime called [GMRT](https://github.com/YoYoGames/GMRT-Beta/blob/main/docs/introduction/GMRT-beta-intro-and-setup-instructions.md) which changes the way how the runtime works for it, and terms like VC and YYC compiler will be depracated.
When it comes out, more advanced features will be added, but it's a plan to keep simple and only include packages from the default runtime configuration
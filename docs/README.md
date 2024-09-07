# About
This game is a submission to the [Spooktober 6th Annual Visual Novel Jam](https://itch.io/jam/spooktober-2024).

[GDD](GDD.md)

[Roadmap](ROADMAP.md)

# Contributing
Contributions should be limited to game jam members. If you're interested in contributing, contact the repository owner.

## Developer setup
See [documentation here.](DEV_SETUP.md) Feel free to reach out to TJ if you need any help!

## Git workflow
Directly committing to main is not allowed. Development work should be done in a branch, then a PR created to merge to main. Squashing commits and rebasing to main is optional but recommended.

### branch naming
For feature work, `feature/<feature-description>` is recommended but not required. For instance, `feature/chapter-3` or `feature/save-system`.
For bug fixes, `bugfix/<bug-number-issue-desc>` is recommended. For instance, `bugfix/issue-1-test-issue`.

## Ren'Py conventions
Follow the [Ren'Py documentation](https://www.renpy.org/doc/html/#) when possible.
As a general rule, keep 1 label to 1 file. It's ok to group several intimately tied labels into 1 file though.
Try not to store anything in the top level directories. Organize assets and .rpy files in directories grouped by type, then context as much as possible.

# Build
Still working on build workflow. Most likely, there will be a .sh script that can be used to create the Windows, macOS, and web versions. Looking into github actions to tick up the version and maybe even create the binaries and upload to itch.io.

## Development Builds
For most development, pressing Play in the Ren'Py launcher is sufficient.

## Releases
Create a Release tag of the intended version. For instance, `release/0.1.0`.

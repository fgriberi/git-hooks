# git-hooks

scripts to be used as git hooks

## Install
Inside a python virtual environment, to Install or update hooks, just run:

`curl -S https://raw.githubusercontent.com/fgriberi/git-hooks/master/hook-me.py | python`

## Flake8
The `hook-me` copy the `.flake8` config file in `$HOME`. So, you can change the config parameters editing this file. 
Flake8 is run per each file that was updated in the current commit. To change this options, and configure the source and test folders of your project for example, just edit the pre-commit.

## Use examples

### pre-commit
TODO

### prepare-commit-msg
TODO

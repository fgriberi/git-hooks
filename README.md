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
This hook runs two verifications.
1. Checks that you commit has not ipdb or pdb statements. If were the case, you'll see on the bash the specific line and position where the statement was not deleted and the commit will be declined. 

![alt text](https://preview.ibb.co/iJgmP7/pdb.png)

2. Checks that you commit pass the `flake8` rules. If the execution fails, then the errors will be shown in the bash and the commit will be declined. 

![alt text](https://image.ibb.co/dcP6P7/flak8.png)

### prepare-commit-msg
As you can see in the picture, the prefix branch pattern name `XXX-1` is added as a prefix commit message.
![alt text](https://image.ibb.co/ndxLZ7/bash.png)


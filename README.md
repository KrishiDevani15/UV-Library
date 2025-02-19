
# UV Documentation

A single replacement tool of `pip`,`virtualenv`.Reason is UV is written in RUST Language.


## Documentation
Here is the Documentation Link 👉🏻 [Documentation](https://linktodocumentation)


## Installation

Installation Process 
- By CURL
```bash
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
```
- By Powershell
```bash
# On Windows.
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
- By Simple PIP Command
```bash
pip install uv
```
    
## UV Command List [OPTIONAL]

- Run only uv in terminal:
```bash
> uv
```
- Usage: 
```bash
> uv [OPTIONS] <COMMAND>
```
- Commands List:
```bash
Commands:
  run      Run a command or script
  init     Create a new project
  add      Add dependencies to the project
  remove   Remove dependencies from the project
  sync     Update the project's environment
  lock     Update the project's lockfile
  export   Export the project's lockfile to an alternate format
  tree     Display the project's dependency tree
  tool     Run and install commands provided by Python packages
  python   Manage Python versions and installations
  pip      Manage Python packages with a pip-compatible interface
  venv     Create a virtual environment
  build    Build Python packages into source distributions and wheels
  publish  Upload distributions to an index
  cache    Manage uv's cache
  self     Manage the uv executable
  version  Display uv's version
  help     Display documentation for a command
```
- Note `uv has no Python Dependencies so we can install this separate to python itself that's going to help us to avoid the need to manage different python installations to check which type of python versions are have 👇🏻`
```bash
uv python list
```

## Project Management
- Project Initialisation 

```bash
# a) Not specific python version 👉🏻 uv init <project_name>
eg uv init example
```
![App Screenshot](https://github.com/user-attachments/assets/c73e0877-2b56-4817-9268-7f7572ae2d92)
```bash
# B) Specific python version 👉🏻 uv init --<python version> <project_name>
eg uv init --python 3.13 example
```
![App Screenshot](https://github.com/user-attachments/assets/877677ec-c81f-404d-b828-263cc0ecb7aa)


## Apply this END-TO-END Project Management
- Project Initialisation 

```bash
eg uv init alchemyK12-ai
```
- Now Add all the Dependencies that we want 👉🏻 uv add <package_name>

```bash
eg uv add fastapi sqlalchemy alembic uvicorn
```

![App Screenshot](https://github.com/user-attachments/assets/d6d6d4fd-f8d2-4339-9f85-0342c99fa0b3)
- Note `uv going to make sure that the .venv folder will be automaticallt add in .gitignore file so not going to push ths code from our virtual environment`
`1) Create own Dependencies List by its own`

`2) Also Create uv.lock file verify what versions of all the Dependencies and sun-Dependencies required for my project`

- Run project 👉🏻 uv run <command>
```bash
eg uv run uvicorn main:app --reload
```
- Sync project .venv with other and download all the Dependencies by it own  
```bash
eg uv sync
```
## Dependencies for  Development Project
- To add a development dependence, include the ` --dev` 
```bash
eg uv add pytest --dev
```
![App Screenshot](https://github.com/user-attachments/assets/a64c8ae9-20fc-4dc4-91fb-172fff96ed4c)

## Remove Dependencies
- To remove a dependence, include the `remove` 
```bash
eg uv remove sqlalchemy alembic
```
- To remove a development dependence, include the `remove --dev` 
```bash
eg uv remove pytest --dev
```
## To See Dependencies Tree
- To remove a dependence, include the `tree` 
```bash
eg uv tree
```




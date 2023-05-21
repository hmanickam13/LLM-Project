## Prerequisites
- `python3.10`

## Required configuration for development:
- OpenAI Key
- URL to the DB (URL provided in `.env.example`)

Make a copy of `.env.example`, rename it to `.env`, and configure the above variables.

## Local development

Initial setup:<br>
Creates and activate a virtual env, install python, pip and all required dependencies for this project.
```sh
$ ./scripts/setup.sh
```

Run local instance:<br>
A streamlit web app should launch on your default browser.
```sh
$ python config.py
```

### Test case queries
WIP

### Extra Commands (MacOS)
List venv using conda:
```sh
$ conda info --envs
```
Switch venv using conda:
```sh
conda activate <-venv-name->
```
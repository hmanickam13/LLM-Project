## Prerequisites
- `python3.10`

## Required configuration for development:
- OpenAI Key
- URL to the DB (URL provided in `.env.example`)

Make a copy of `.env.example`, rename it to `.env`, and configure the above variables.

## Local development

Initial setup:<br>
Create a virtual env with python & pip. I used conda package manager. Feel free to use a package manager of your choice.
```sh
$ conda create --name testvenv python=3.10 pip
```

Activate the virtual env.
```sh
$ conda activate testvenv
```

Install all required dependencies for this project
```sh
$ ./scripts/setup.sh
```

Run local instance:<br>
A streamlit web app should launch on your default browser.
```sh
$ python app/config.py
```

### Test case queries
1. What was the top performing ETF last year?
2. Did spy outperform tlt in 2020 and 2021?
3. What was the worst performing ETF every year for the past 5 years?

### Extra Commands (MacOS)
List venv using conda:
```sh
$ conda info --envs
```
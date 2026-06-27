# QA Engineer Home Assignment

## Overview

This repository contains:

* Manual test plan
* Test execution results and bug reports
* UI automation tests
* API automation tests
* Test strategy and recommendations

The application under test simulates a sports betting workflow.

## Tech Stack

* Python 3.12
* Selenium WebDriver
* Pytest
* Requests
* Chrome Browser

## Project Structure

```text
docs/
pages/
api/
tests/
utils/
```

## Installation
### uv
```bash
git clone https://github.com/alex-pancho/sporty_home_task.git
cd sporty_home_task

uv sync
```

### pip

```bash
git clone https://github.com/alex-pancho/sporty_home_task.git
cd sporty_home_task


python -m venv venv

source venv/bin/activate
# Windows:
venv\Scripts\activate

pip install -r requirements.txt
```

## Run UI Tests

```bash
pytest tests/ui -v
```

## Run API Tests

```bash
pytest tests/api -v
```

## Run All Tests

```bash
pytest -v
```


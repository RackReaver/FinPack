![Alt text](logo.png?raw=true "logo")

# Personal Finance Package (FinPack)

Super simple personal finance tracking/management tools.

Build balance sheets and cashflow statements.

Chart your net worth, asset allocation, financial independence trajectory and much more.

---

## Table of Contents

- [Installation](#installation-for-development)
- [Tests/Coverage](#running-tests-and-checking-coverage)
- [Deployment](#deployment)
- [How to Use](#how-to-use)
- [Contributing](#contributing)
- [Versioning](#versioning)
- [Authors](#authors)

---

## Installation (for development)

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

1. Fork this repo
2. Install [Git](https://git-scm.com/downloads), [Python 3.9+](https://www.python.org/downloads/) and [Poetry](https://python-poetry.org/docs/#installation)
3. Clone the newly forked repo to your computer
4. Inside `FinPack/` run `poetry install`

## Running Tests and Checking Coverage

Tests are created using unittest but are run with pytest (ensure you follow the [Installation (for development)](#installation-for-development) steps before running tests and checking test coverage):

```
$ poetry run pytest -v --cov
```

## Deployment

This package can be installed with the following command:

```
pip install git+github.com/RackReaver/finpack.git
```

## How To Use

TBA, the command line interface has not yet been created.

```
  ______ _       _____           _
 |  ____(_)     |  __ \         | |
 | |__   _ _ __ | |__) |_ _  ___| | __
 |  __| | | '_ \|  ___/ _` |/ __| |/ /
 | |    | | | | | |  | (_| | (__|   <
 |_|    |_|_| |_|_|   \__,_|\___|_|\_\\
```

## Contributing

Please read [CONTRIBUTING.md](#) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/RackReaver/FinPack/tags).

## Authors

- **Matt Ferreira** - _Developer_ - [RackReaver](https://github.com/RackReaver)

See also the list of [contributors](#) who participated in this project.

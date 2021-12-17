![Alt text](https://github.com/RackReaver/FinPack/raw/main/logo.png?raw=true)

# Personal Finance Package (FinPack)

Super simple personal finance tracking.

Build balance sheets and cashflow statements.

Chart your net worth, asset allocation, financial independence trajectory and much more.

---

## Demo

![Demo gif](https://github.com/RackReaver/FinPack/raw/main/demo.gif)

## Table of Contents

- [Installation](#installation-for-development)
- [Running Tests and Checking Coverage](#running-tests-and-checking-coverage)
- [Deployment](#deployment)
- [How to Use](#how-to-use)
  - [Generating the boilerplate data.csv](#generating-the-boilerplate-datacsv)
  - [Manually adding data to data.csv](#manually-adding-data-to-datacsv)
  - [Account Structure in data.csv](#account-structure-in-datacsv)
  - [Example CSV](#example-csv)
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
pip install finpack
```

## How To Use

```
  ______ _       _____           _
 |  ____(_)     |  __ \         | |
 | |__   _ _ __ | |__) |_ _  ___| | __
 |  __| | | '_ \|  ___/ _` |/ __| |/ /
 | |    | | | | | |  | (_| | (__|   <
 |_|    |_|_| |_|_|   \__,_|\___|_|\_\

Super simple personal finance tracking/management tools.

Commands:
    init        Generate boilerplate data.csv
    balsheet    Outputs balance sheet to terminal

Usage:
    finpack init [--filepath=filepath] [--sample-dataset] [--overwrite]
    finpack balsheet [--filepath=filepath] [--levels=level] [--date=date]
    finpack (--version | --help | -h)

Options:
    --filepath=filepath         Location of the account list. [default: data.csv]
    --levels=level              How deep of a breakdown on the report [default: 3]
                                    1 Categories
                                    2 Categories + Sub-categories
                                    3 Categories + Sub-categories + accounts
    --overwrite                 Write over existing file
    --date=date                 Custom date to build report (YYYY-MM-DD) [default: today]
    -v --version                Display installed version
    -h --help                   Show available commands
```

### Generating the boilerplate data.csv:

The following will generate `data.csv`.

```
finpack init

or

finpack init --filepath=data.csv
```

### Manually adding data to `data.csv`:

Data can be added manually to this csv file as long as you follow these standards:

- Duplicate account names are only permitted if account types are different
- Account types are always lowercase
- Dates are always formatted `YYYY-MM-DD`

### Account Structure in `data.csv`:

| Types        | Description                                                         |
| ------------ | ------------------------------------------------------------------- |
| account      | Determined and configured by user (examples below)                  |
| type         | Pre-determined values (assets, liabilities, incomes, expenses)      |
| category     | Determined and configured by user (examples below)                  |
| sub_category | Determined and configured by user (examples below)                  |
| description  | Determined and configured by user, best for supplement account data |

### Example CSV:

This is an example print out of what `finpack init --sample-dataset` will output to `data.csv`

`YYYY-MM-DD` is set dynamically when using `finpack init` and will be the current date.

| account                    | type      | category                  | sub_category     | description | YYYY-MM-DD |
| -------------------------- | --------- | ------------------------- | ---------------- | ----------- | ---------- |
| Checking Account 1         | asset     | Cash and Cash Equivalents | Checking Account |             | 1000.00    |
| Checking Account 2         | asset     | Cash and Cash Equivalents | Checking Account |             | 2000.00    |
| Savings Account 1          | asset     | Cash and Cash Equivalents | Savings Account  |             | 5000.00    |
| Retirement Savings Account | asset     | Retirement Accounts       | 401(k)s          |             | 20000.00   |
| 123 Main St.               | asset     | Property                  | Real Estate      |             | 200000.00  |
| 123 Main St.               | liability | Loans and Mortgages       | Mortgages        |             | 150000.00  |
| Student Loan 1             | liability | Loans and Mortgages       | Student Loans    |             | 10000.00   |
| Student Loan 2             | liability | Loans and Mortgages       | Student Loans    |             | 10000.00   |

## Contributing

Please read [CONTRIBUTE](CONTRIBUTE.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/RackReaver/FinPack/tags).

## Authors

- **Matt Ferreira** - _Developer_ - [RackReaver](https://github.com/RackReaver)

See also the list of [contributors](#) who participated in this project.

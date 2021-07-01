# FinPack

Super simple financial tracking/management tools.

## Table of Contents

- [Installation](#installation)
- [Running Tests and Checking Coverage](#running-tests-and-checking-coverage)
- [How to Use](#how-to-use)
  - [Folder Structure](#folder-structure-financials)
  - [Accounts YAML File Structure](#accounts-yaml-file-structure)
  - [Example Accounts YAML File](#example-accounts-yaml-file-accountsyaml)
- [ToDo](#to-dos)
- [Authors](#authors)
- [License](#license)

## Installation

This package can be installed with the following command:

```
pip install git+github.com/RackReaver/finpack.git
```

## Running Tests and Checking Coverage

```
>>> coverage run -m pytest
>>>
>>> coverage report
```

## How To Use

```
$ finpack --help
 ______ _       _____           _
|  ____(_)     |  __ \         | |
| |__   _ _ __ | |__) |_ _  ___| | __
|  __| | | '_ \|  ___/ _` |/ __| |/ /
| |    | | | | | |  | (_| | (__|   <
|_|    |_|_| |_|_|   \__,_|\___|_|\_\

Super simple financial tracking/management tools.

Commands:
  init  Build sample accounts.yaml file
  run   Update account values interactively

Usage:
    finpack init [--filepath=filename] [--overwrite]
    finpack run [--filepath=filename] [--date=date]

Options:
    --filepath=filename        Location of the account list [default: accounts.yaml]
    --date=date                Custom date to run against (YYYY-MM-DD). [default: today]
    --overwrite                Write over existing file
```

### Folder Structure `financials`:

```
financials/
|
+-- accounts.yaml   # Contains current account names
+-- data.json       # Historical data (auto-generated)

```

### Accounts YAML File Structure:

| Types        | Description                                                    |
| ------------ | -------------------------------------------------------------- |
| root_type    | Pre-determined values (assets, liabilities, incomes, expenses) |
| category     | Determined and configured by user (exampes below)              |
| sub_category | Determined and configured by user (exampes below)              |
| account      | Determined and configured by user (exampes below)              |

```
assets:
^  Cash and Cash Equivalents:
|  ^  Cash:
|  |  ^ - Wallet
|  |  |   ^
|  |  |   |
|  |  |   +-- account
|  |  |
|  |  +------ sub_category
|  |
|  +--------- category
|
+------------ root_type
```

### Example Accounts YAML File `accounts.yaml`:

```
assets:
  Cash and Cash Equivalents:
    Cash:
      - Wallet
    Checking Accounts:
      - Bank of America
      - Chase
      - Charles Schwab
    Savings Accounts:
      - Bank of America (Cash Reserve)
    Other:
      - Paypal
      - Venmo
  Taxable Accounts:
    Brokerage Accounts:
      - Robinhood
      - Coinbase
    Online Funds:
      - Fundrise
      - Lending Club
  Tax-Advantaged Accounts (Retirement Accounts):
    401(k)s:
      - Vanguard
    IRAs:
      - Fidelity (Roth IRA)
  Property:
    Real Estate:
      - Primary Residence
      - Investment Property
    Jewlery, Watches and Luxury Goods:
      - Tag Heuer Watch
      - Gold Chain
    Vehicles:
      - Primary Car
      - Recreational Car
  Other Assets:
    Life Insurance:
      - MassMutual Cash Value
    Monies Owed:
      - Parents
      - Friend
liabilities:
  Short-Term Credit:
    Short-Term Credit:
      - Credit Card 1
      - Credit Card 2
    Loans and Mortgages:
      - Primary Residence
      - Investment Property
      - Student Loan 1
      - Student Loan 2
    Other Liabilities:
      - Other 1
      - Other 2
  Loans and Mortgages:
    Real Estate:
      - Primary Residence
      - Investment Property
    Student Loans:
      - Student Loan 1
      - Student Loan 2
    Auto Loans:
      - Primary Car
      - Recreational Car
```

## To-Dos

- [] Build app models
- [] Generate a model that allows for multi-level accounts
- [] Accept .yaml format
- [] Accept .json format

## Authors

- **Matt Ferreira** - _Developer_ - [RackReaver](https://github.com/RackReaver)

## License

This project is licensed under the Apache License - see the [LICENSE](LICENSE) file for details

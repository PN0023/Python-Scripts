# Python Scripts

Welcome to my Python scripting repository! This repository contains various Python scripts demonstrating my skills in automation, web scraping, and mathematical computations.

## Table of Contents

- [Overview](#overview)
- [Scripts](#scripts)
  - [Google Job Search and Save](#google-job-search-and-save)
  - [Prime Number Utilities](#prime-number-utilities)
- [Installation & Requirements](#installation--requirements)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

This repository contains Python scripts developed for different purposes, including web scraping and mathematical calculations. Below is a brief description of the scripts included.

## Scripts

### Google Job Search and Save

This script performs a Google search for programming job postings based on specified keywords and stores relevant results in a CSV file.

#### Features:

- Searches for programming job postings using Google search.
- Extracts relevant links containing specified keywords.
- Saves the results in a CSV file for easy reference.

#### Technologies Used:

- `googlesearch`
- `re` (Regular Expressions)
- `csv`
- `datetime`

#### Example Query:

```python
query = "stellenangebote programmierer \"PLC""
keywords = ["python", "django"]
```

### Prime Number Utilities

This script provides utility functions to check for prime numbers and find the largest prime number up to a given limit.

#### Features:

- Checks if a number is prime.
- Finds the largest prime number below a given number.

#### Technologies Used:

- `math`
- `datetime`
- Recursive and iterative prime number checking.

## Installation & Requirements

To run these scripts, ensure you have Python installed along with the necessary dependencies.

### Install Dependencies:

```sh
pip install googlesearch-python
```

## Usage

Clone the repository and run the scripts as needed.

```sh
git clone https://github.com/yourusername/your-repository.git
cd your-repository
python script_name.py
```

Modify the scripts as needed to suit your use case.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve these scripts.

## License

This repository is licensed under the MIT License. See `LICENSE` for details.


# Opulus ![last commit](https://img.shields.io/github/last-commit/zobweyt/opulus) ![license](https://img.shields.io/github/license/zobweyt/opulus)

Gudgeon is a multi-purpose Telegram bot. It is an open-source project, allowing all of the community's members to contribute and see their code live in action. 

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#key-features">Key Features</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#contribution">Contribution</a></li>
  </ol>
</details>



## Key Features
* Send pictures of cats and dogs
* Weather anywhere by its destination or location.
* Using the [Wallhaven API](https://wallhaven.cc/help/api) to add an appropriate picture to the weather.



## Getting started

Clone the repository:
```sh
git clone https://github.com/zobweyt/opulus.git
```

Install common project dependencies locally:
```sh
pip install -r requirements/common.txt
```

Create an `.env` file in `src/opulus` directory and configure the environment variables:
```dotenv
TOKEN=""
OWM_API_KEY=""
```

Finally, run the telegram bot:
```sh
python main.py
```

## Contribution

Feel free to open an issue, contribute or suggest new ideas to improve this repository!

Install project dependencies required for development locally:
```sh
pip install -r requirements/dev.txt
```

Before committing, run static analysis tools in the project root directory:
```sh
black .
flake8
```
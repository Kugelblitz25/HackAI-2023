# Installation

## Using Virtual Environment (Recommended)

```bash
python -m venv venv
venv\scripts\activate
pip install -r requirements.txt
```

## Getting API keys

- Go to [Fixer API Website](https://apilayer.com/marketplace/fixer-api?utm_source=apilayermarketplace&utm_medium=featured). 

- Subscribe for the Free Plan of the API to get an API key.

- Copy the API key.

## Setup

In .env file in the main directory and add the API_KEY as shown below

```
API_KEY=your_api_key
```

## Running Agent

```bash
python src/main.py
```

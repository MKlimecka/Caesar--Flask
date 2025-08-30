# Caesar- Flask

A small web aplication with Flask, for encrypting and decrypting text with Caesar cipher. 
An educational project.

## Features
- Encypt and decrypt text using the Caesar cipher
- Optionally support Polish characters
- Simple web interface built with Flask
- Unit tests with pytest and HTML parsing with beautifulsoup4

## Requirements
- Python 3.8+
- Virtual envirnonment (recommended)

Main dependencies:
- Flask
- pytest
- beautifulsoup4

(Install all dependencies with 'requirements.txt.')

## Installation and setup

1 Clone this repository:

```bash
git clone https://github.com/MKlimecka/Caesar--Flask
```

2 Create and activate a virtual environment:

```bash
python -m  venv venv
source venv/bin/activate   # on Linux/Mac
venv\Scripts\activate      # on Windows
```

3 Install dependecies:

```bash
pip install -r requirements.txt
```

## Running the aplication
Start the flask development server:

```bash
flask run
```

or 

```bash
python app.py
```

## Running tests
Run all tests with:

```bash
pytest
```

## Deployment
The project can be deployed to cloud platforms like Render.
Deployment instructions will be added later.

 ## License
MIT License
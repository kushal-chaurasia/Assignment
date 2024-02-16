# Supermarket Checkout System

This is a Python implementation of a supermarket checkout system that calculates the total price of items in a cart based on provided pricing rules.

## Setup

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:

    ```bash
    cd supermarket-checkout-system
    ```

3. (Optional) Set up a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

You can run the tests using pytest:

```bash
pytest
```

To run python script

```
python main.py
```

## Build the Docker image:

    ```bash
    docker build -t supermarket-checkout .
    ```

## Run the Docker container:

    ```bash
    docker run --rm supermarket-checkout
    ```
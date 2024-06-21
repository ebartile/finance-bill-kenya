# Finance Bill 2024 Kenya Feedback

This Streamlit application fetches the Finance Bill 2024 PDF file from the Kenya Law website, extracts its text, and retrieves feedback using the Gemini API.

## Features

- Automatically fetches the Finance Bill 2024 PDF from a predefined URL.
- Extracts text content from the PDF.
- Sends the extracted text to the Gemini API for feedback.
- Displays the extracted text and feedback in a user-friendly interface.

## Requirements

- Python 3.7 or higher
- Streamlit
- PyPDF2
- Requests

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/ebartile/finance-bill-kenya.git
    cd finance-bill-kenya
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

## Configuration

1. Create a `secrets.toml` file in the root directory of the project:

    ```toml
    [gemini]
    api_key = "your_gemini_api_key"
    ```

2. Make sure to add `secrets.toml` to your `.gitignore` file to avoid pushing it to GitHub:

    ```sh
    echo "secrets.toml" >> .gitignore
    ```

## Running the App

1. Run the Streamlit app:

    ```sh
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501` to view the app.

## Deployment

To deploy the app on Streamlit Cloud:

1. Push your code to GitHub.
2. Go to [Streamlit Cloud](https://share.streamlit.io/) and sign in with your GitHub account.
3. Create a new app, connect your GitHub repository, and specify the branch and main file path (`app.py`).
4. Add your secrets in the Streamlit Cloud settings under the "Secrets" tab:

    ```toml
    [gemini]
    api_key = "your_gemini_api_key"
    ```

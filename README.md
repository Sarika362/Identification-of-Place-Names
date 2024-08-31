# Identification of Place Names in a Natural Language Sentence

This project utilizes the Streamlit web framework combined with Natural Language Processing (NLP) techniques to identify place names within natural language sentences. The application allows users to input text and receives translations and place names identification in return.

![image](https://github.com/user-attachments/assets/c5d61162-ed68-4f04-b99e-dd2899412fd4)

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:
- Python 3.x
- Required Python libraries (listed in `requirements.txt`)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/YourUsername/Place-Name-Identification.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Place-Name-Identification
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

To start the application, run:
```bash
streamlit run app.py
```

## Running the Application

The app will be accessible at [http://localhost:8501/](http://localhost:8501/).

## 🛠️ Usage

- Enter your text into the input box (which can contain place names).
- Click on the "Submit" button.
- The app will display the place names found in your input text along with their canonical names and their category (Country, State, or City).

## 📂 Project Structure

- `app.py`: Main Streamlit application file with user interface and functionality.
- `NewModel.py`: Contains functions for place name identification using NLP.
- `Fuzzer.py`: Includes fuzzy matching functions to find closest place names.
- `Translator.py`: Provides translation functionality using Google Translator.
- `places.csv`: Dataset containing place names categorized by country, state, and city.

## 💡 Credits

Developed by Sarika M N

## 🤝 Contributing

Feel free to open issues or submit pull requests to improve this project!

---

Thank you for checking out the Identification of Place Names project! 🙌

# Text and Image Generation Project

## Overview

This project aims to showcase the capabilities of text and image generation using Replicate and Streamlit. Replicate is used for generating text, while Streamlit provides a user-friendly interface to interact with and visualize the generated content.


## Features

- **Text Generation**: Utilizes Replicate to generate creative and diverse text content based on given prompts.

- **Image Generation**: Incorporates Replicate for image synthesis, creating unique and imaginative visuals.

- **User Interaction**: Streamlit provides a user-friendly interface to customize prompts, view generated results, and control parameters.


## File Structure
```md
.
├── __pycache__                   # Python bytecode cache (automatically generated)
├── pages                         # Directory for Streamlit pages (if applicable)
│   └── ...                       # Additional files related to Streamlit pages
├── venv                          # Virtual environment directory (if using virtual environment)
│   └── ...                       # Virtual environment files
├── 1_Text Gen.py                 # Main script for Text Generation
├── replicateBackend.py           # Utility script for interacting with Replicate API
├── requirements.txt              # Project dependencies
└── README.md                     # Project documentation

```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Xyz31/LLM_Text_And_Image_Generation-Project.git
   ```

2. Change into the project directory:
    ```bash
      cd LLM_Text_And_Image_Generation-Project.git
   ```
3. Install the required dependencies:

  ```bash
    pip install -r requirements.txt

  ```
4. Run the Streamlit app:

  ```bash
    streamlit run app.py
  ```
5. Open your web browser and navigate to http://localhost:8501 to interact with the application.


# LAWGPT

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/Sameeruddinmd8/LawGPT.svg)](https://github.com/Sameeruddinmd8/LawGPT/stargazers)

![Lawgpt](https://github.com/Sameeruddin8/LawGPT/assets/102674044/0fe192b9-8723-4620-943b-39dbf9c87757)


**LAWGPT** is an innovative project that leverages the power of Language Models, including OpenAI's GPT, to provide automated legal document analysis and retrieval of answers to legal queries. It's built using [LangChain](https://langchain.org/) and integrates OpenAI's API for efficient information retrieval. Additionally, this project utilizes the open-source embedding model `intfloat/multilingual-e5-large` to facilitate the embedding of legal documents.



## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Embedding Script](#running-the-embedding-script)
  - [Running the Application](#running-the-application)
- [Conclusion](#conclusion)

## Getting Started

These instructions will help you get started with setting up and using LAWGPT.

### Prerequisites

Before you begin, ensure you have the following requirements:

- Python 3.7+
- Git

### Installation

1. Clone this repository to your local machine using:

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   ```

2. Navigate to the project directory:

   ```bash
   cd your-repo
   ```

## Usage

LAWGPT consists of two main components: an embedding script and an application for legal document analysis. Follow the steps below to use the project.

### Running the Embedding Script

The embedding script is used to preprocess and embed legal documents for efficient retrieval. Execute the following command:

```bash
python embedding.py
```

This script will process your legal documents using the `intfloat/multilingual-e5-large` embedding model and store the embeddings for later use in the application.

### Running the Application

The LAWGPT application allows users to ask legal questions and retrieve relevant answers from the embedded legal documents. To start the application, run:

```bash
python app.py
```

The application will be accessible at `http://localhost:5000` by default. Open your web browser and navigate to this address to interact with the LAWGPT application.

## Conclusion

LAWGPT is a powerful tool that simplifies legal document analysis and provides accurate answers to legal queries. By combining state-of-the-art language models and efficient embedding techniques, it streamlines the legal research process. Use this project to enhance your legal research capabilities and save valuable time.

Feel free to contribute to the project, report issues, or suggest improvements. Your feedback and contributions are highly appreciated!

# Project Similarity Calculator

## Overview
This project calculates the semantic similarity between a new project description and existing project descriptions using the Universal Sentence Encoder from TensorFlow Hub. By comparing the embeddings of different project descriptions, it determines the degree of similarity between them.

## Requirements
- Python 3.x
- TensorFlow Hub
- NumPy library

```
pip install -r requirements.txt
```

## How it works
1. **Universal Sentence Encoder**: The project utilizes the Universal Sentence Encoder module from TensorFlow Hub to generate embeddings for project descriptions. This module encodes text into high-dimensional vectors capturing semantic information.
2. **Semantic Similarity Calculation**: The semantic similarity between two project descriptions is calculated using the dot product of their respective embeddings. A higher dot product indicates greater semantic similarity.
3. **Percentage Similarity**: The similarity score is converted to a percentage, indicating the degree of similarity between the project descriptions.

## Usage
1. Ensure you have Python installed on your system.
2. Install the required libraries: `tensorflow-hub`, `numpy`.
3. Run the `calculate_similarity.py` script.
4. Input the new project description and compare it with existing project descriptions.
5. The program will output the percentage similarity between the new project description and each existing project description.

import tensorflow_hub as hub
import numpy as np

# Load Universal Sentece Encoder module
embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

def calculate_semantic_similarity(text1, text2):
  # Get embeddings 
  embeddings = np.array(embed([text1, text2]))

  # Calculate similarity score
  similarity_score = np.dot(embeddings[0], embeddings[1])

  return similarity_score


descriptions = {
  'projeto 1': """The Email Handling API developed with GoLang provides a lightweight and high-performance solution for managing email communication within applications. Leveraging GoLang's concurrency features and efficient runtime, the API offers fast and scalable email processing capabilities suitable for handling high volumes of traffic.
  The API integrates seamlessly with email service providers such as Gmail, Outlook, and SendGrid, enabling developers to send and receive emails programmatically with ease. Built-in support for concurrency and parallelism in GoLang allows the API to handle multiple email requests concurrently, maximizing throughput and responsiveness.
  Furthermore, the simplicity and readability of GoLang's syntax make it easy for developers to understand and maintain the codebase. With its small memory footprint and fast execution speed, the GoLang-based Email Handling API is well-suited for resource-constrained environments and applications where performance is critical.
  In summary, the Email Handling API developed with GoLang offers a powerful and efficient solution for managing email communication, making it an ideal choice for building scalable and reliable email-related features in modern applications.""",
  'projeto 2': """The Image Recognition API developed with Python leverages machine learning and computer vision techniques to provide accurate and reliable image recognition capabilities. By utilizing pre-trained deep learning models such as Convolutional Neural Networks (CNNs), the API can identify objects, scenes, and patterns within images with high precision.""",
  'projeto 3': """The Payment Gateway API developed with Node.js offers a secure and flexible solution for processing online payments within web and mobile applications. With support for multiple payment methods, including credit cards, digital wallets, and bank transfers, the API enables seamless and convenient transactions for users across various platforms.""",
  'projeto 4': """The Email Handling API developed with NestJS is a robust solution for managing email communication within applications. Built on top of the Node.js runtime, NestJS provides a modular and scalable framework for building efficient server-side applications. The API integrates seamlessly with popular email service providers such as Gmail, Outlook, and SendGrid, allowing developers to send and receive emails programmatically.
  The API exposes endpoints for composing and sending emails, as well as retrieving and processing incoming messages. Leveraging NestJS's built-in dependency injection and middleware capabilities, the API ensures secure and reliable email transmission while adhering to industry best practices for authentication and authorization.
  Furthermore, the NestJS framework's support for TypeScript enables developers to write clean, type-safe code, reducing errors and improving maintainability. With its intuitive syntax and extensive documentation, NestJS facilitates rapid development of email-related features, making it an ideal choice for modern web applications."""
}

new_project_description = """The Email Handling API developed with GoLang provides a lightweight and high-performance solution for managing email communication within applications. Leveraging GoLang's concurrency features and efficient runtime, the API offers fast and scalable email processing capabilities suitable for handling high volumes of traffic."""

for project, description in descriptions.items():
  # Calculate semantic similarity between the new project description and each existing description
  similarity_score = calculate_semantic_similarity(new_project_description, description)
  print(f"Similarity score between new project and {project}: {(similarity_score * 100):.2f}%")
# README
## Dev Note 

I have not used any DB for faster prototyping

## Project Overview

This project aims to develop a system capable of processing natural language queries and providing responses in a conversational manner. The system leverages pre-trained language models, embeddings, and a vector database to store and search document embeddings for relevant information. The key components include loading documents, creating embeddings, storing and searching embeddings, and generating context-aware responses. A Flask web application has been developed to offer an interactive interface and API-based access to the system's features.

## Features

- **Document Loading and Processing**: Upload and process PDF documents by splitting them into smaller chunks.
- **Embeddings Creation**: Generate embeddings for each text chunk using a pre-trained model.
- **Embeddings Storage and Search**: Store embeddings in a ChromaDB database and retrieve relevant information based on queries.
- **Conversational Interaction**: Generate responses to user queries based on contextual embeddings using a conversational interface exposed via a Flask API.
- **RESTful API**: Access the system's capabilities via endpoints for chat initiation, messaging, and document processing.

## Setup and Installation

1. **Clone the Repository**:

    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Install Dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

3. **Setup Configuration**:

    Ensure the following configurations in `config/config.py`:
    - `UPLOAD_FOLDER`: Directory for uploaded files.
    - `ALLOWED_EXTENSIONS`: Set of allowed file extensions (e.g., `['pdf']`).

4. **setup .env**:

    Only required varaible is GEMINI_API that can be access by gemini api docs 

## Quick test

You can run the test.py file for a quick test of all API

## Usage

### API Endpoints

The Flask web application provides several API endpoints:

#### 1. **Start a New Chat Thread**

   **Endpoint**: `/api/chat/start`  
   **Method**: `POST`  
   **Description**: Initializes a new chat thread for a given asset.  
   **Request Body**:
   ```json
   {
     "asset_id": "<asset_id>"
   }
   ```
   **Response**:
   ```json
   {
     "chat_thread_id": "<unique_chat_thread_id>"
   }
   ```

#### 2. **Send a Message**

   **Endpoint**: `/api/chat/message`  
   **Method**: `POST`  
   **Description**: Sends a message within an existing chat thread and generates a response.  
   **Request Body**:
   ```json
   {
     "chat_thread_id": "<chat_thread_id>",
     "message": "<user_message>"
   }
   ```
   **Response**:
   ```json
   {
     "agent_response": "<generated_response>"
   }
   ```

#### 3. **Retrieve Chat History**

   **Endpoint**: `/api/chat/history`  
   **Method**: `GET`  
   **Description**: Retrieves the chat history for a specific chat thread.  
   **Query Parameter**: `chat_thread_id`  
   **Response**:
   ```json
   {
     "chat_history": [
       {
         "sender": "system",
         "message": "Chat started"
       },
       {
         "sender": "user",
         "message": "<user_message>"
       },
       {
         "sender": "agent",
         "message": "<agent_response>"
       }
     ]
   }
   ```

#### 4. **Process a Document**

   **Endpoint**: `/api/documents/process`  
   **Method**: `POST`  
   **Description**: Processes an uploaded document, creates embeddings, and stores them in the database.  
   **Request**:
   - File upload (using form-data).
   - Ensure the file type is allowed as per `ALLOWED_EXTENSIONS`.  
   **Response**:
   ```json
   {
     "asset_id": "<unique_asset_id>",
     "file_path": "<path_to_uploaded_file>"
   }
   ```

## Design Notes

### Intermediary Representation

The system organizes raw data from web articles and PDF documents into a structured format for efficient storage and retrieval:

1. **Text Splitting**: Splits PDF documents into manageable text chunks.
2. **Embeddings**: Converts text chunks into embeddings using a pre-trained model (`all-MiniLM-L6-v2`).
3. **Metadata Storage**: Stores metadata (e.g., page number, asset ID) alongside embeddings to maintain context.

### Open Source Libraries and Tools

- **Flask**: Used for creating the web application and RESTful API.
- **LangChain**: Facilitates text splitting and document handling.
- **HuggingFace Transformers**: Provides pre-trained models for generating embeddings.
- **ChromaDB**: Stores and retrieves embeddings efficiently.
- **Gemini**: Generates conversational responses based on user input and retrieved context.

## Example Flow

1. **Document Upload**:
   - User uploads a PDF document.
   - The system processes the document, creates embeddings, and stores them in the database.

2. **Start Chat**:
   - User initiates a chat for a specific document (asset).
   - A unique chat thread ID is generated.

3. **Send and Receive Messages**:
   - User sends messages.
   - The system retrieves relevant document embeddings, formulates a response, and stores the conversation history.


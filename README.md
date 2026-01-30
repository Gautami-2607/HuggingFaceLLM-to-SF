# Hugging Face LLM FastAPI Application

A FastAPI application that integrates with Hugging Face LLM models for text generation.

## Features

- **FastAPI Framework**: Modern, fast web framework for building APIs
- **Hugging Face Integration**: Uses Hugging Face Inference API for LLM calls
- **Health Checks**: Built-in health check endpoint
- **CORS Support**: Configured for cross-origin requests
- **Error Handling**: Comprehensive error handling and logging
- **Pydantic Validation**: Request/response validation using Pydantic models

## Project Structure

```
.
├── main.py                      # FastAPI application entry point
├── schemas.py                   # Pydantic models for requests/responses
├── huggingface_service.py       # Hugging Face API integration
├── requirements.txt             # Python dependencies
├── .env                        # Environment variables
└── README.md                   # This file
```

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Update the `.env` file with your Hugging Face API credentials:

```
HUGGINGFACE_API_KEY=your_actual_api_key_here
MODEL_NAME=meta-llama/Llama-2-7b-chat-hf
```

To get your Hugging Face API key:
1. Visit [Hugging Face Hub](https://huggingface.co)
2. Create an account or sign in
3. Go to [Settings > Access Tokens](https://huggingface.co/settings/tokens)
4. Create a new token with "read" access

### 3. Run the Application

```bash
python main.py
```

The API will be available at `http://localhost:8000`

## API Endpoints

### 1. Health Check
- **Endpoint**: `GET /health`
- **Description**: Check if the API is running
- **Response**:
  ```json
  {
    "status": "healthy",
    "message": "API is running successfully"
  }
  ```

### 2. Generate Text
- **Endpoint**: `POST /generate`
- **Description**: Generate text using the Hugging Face LLM
- **Request Body**:
  ```json
  {
    "text": "Your prompt here",
    "max_tokens": 100,
    "temperature": 0.7,
    "top_p": 0.95
  }
  ```
- **Response**:
  ```json
  {
    "generated_text": "Generated response here",
    "model": "meta-llama/Llama-2-7b-chat-hf",
    "prompt": "Your prompt here"
  }
  ```

### 3. Get Model Info
- **Endpoint**: `GET /model`
- **Description**: Get information about the current model
- **Response**:
  ```json
  {
    "model": "meta-llama/Llama-2-7b-chat-hf",
    "description": "Current model used for text generation"
  }
  ```

### 4. Root
- **Endpoint**: `GET /`
- **Description**: Welcome message
- **Response**:
  ```json
  {
    "message": "Welcome to Hugging Face LLM API"
  }
  ```

## Interactive API Documentation

Once the server is running, visit:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Testing with curl

```bash
# Health check
curl http://localhost:8000/health

# Generate text
curl -X POST "http://localhost:8000/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "What is artificial intelligence?",
    "max_tokens": 150,
    "temperature": 0.7,
    "top_p": 0.95
  }'

# Get model info
curl http://localhost:8000/model
```

## Configuration Parameters

### Text Generation Parameters

- **max_tokens**: Maximum number of tokens to generate (default: 100)
- **temperature**: Controls randomness in response (0-1, default: 0.7)
  - Lower values = more deterministic
  - Higher values = more creative
- **top_p**: Nucleus sampling parameter (default: 0.95)
  - Controls diversity via nucleus sampling

## Environment Variables

- `HUGGINGFACE_API_KEY`: Your Hugging Face API token (required)
- `MODEL_NAME`: The model to use (default: meta-llama/Llama-2-7b-chat-hf)

## Error Handling

The API returns appropriate HTTP status codes:
- `200`: Success
- `422`: Validation error
- `500`: Server error (API communication issue)

## Dependencies

- **fastapi**: Web framework
- **uvicorn**: ASGI server
- **huggingface-hub**: Hugging Face API client
- **pydantic**: Data validation
- **python-dotenv**: Environment variable management
- **httpx**: HTTP client

## Notes

- Ensure you have accepted the model license on Hugging Face Hub before using it
- API calls may take time depending on the model size
- Consider implementing rate limiting for production use
- Keep your API key secure and never commit it to version control

## License

This project is open source and available under the MIT License.
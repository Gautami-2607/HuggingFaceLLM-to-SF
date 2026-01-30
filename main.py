from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import logging

from schemas import TextPrompt, TextResponse, HealthResponse
from huggingface_service import generate_text, MODEL_NAME

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Hugging Face LLM API",
    description="FastAPI application that integrates with Hugging Face LLM models",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Root"])
async def root():
    """Root endpoint"""
    return {"message": "Welcome to Hugging Face LLM API"}


@app.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        message="API is running successfully"
    )


@app.post("/generate", response_model=TextResponse, tags=["Generation"])
async def generate_text_endpoint(prompt: TextPrompt):
    """
    Generate text using Hugging Face LLM
    
    Args:
        prompt: TextPrompt object containing the input text and parameters
        
    Returns:
        TextResponse object with generated text
    """
    try:
        logger.info(f"Received prompt: {prompt.text}")
        
        # Call the Hugging Face service
        generated_text = generate_text(
            prompt=prompt.text,
            max_tokens=prompt.max_tokens,
            temperature=prompt.temperature,
            top_p=prompt.top_p
        )
        
        logger.info("Text generation completed successfully")
        
        return TextResponse(
            generated_text=generated_text,
            model=MODEL_NAME,
            prompt=prompt.text
        )
    except RuntimeError as e:
        logger.error(f"Hugging Face API error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get("/model", tags=["Info"])
async def get_model_info():
    """Get information about the current model"""
    return {
        "model": MODEL_NAME,
        "description": "Current model used for text generation"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

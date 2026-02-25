#!/usr/bin/env python3
"""
Convenient script to run the Mergington High School Activities application.
"""

import uvicorn

if __name__ == "__main__":
    print("Starting Mergington High School Activities API...")
    print("Server will be available at: http://localhost:8000")
    print("API documentation: http://localhost:8000/docs")
    print("Press CTRL+C to stop the server")
    
    uvicorn.run("src.app:app", host="0.0.0.0", port=8000, reload=True)

import os

class Config:
    GRADIENTAI_API_URL = os.getenv('GRADIENTAI_API_URL', 'https://api.gradientai.com/llama-3-8b-instruct-gradient-1048k')
    
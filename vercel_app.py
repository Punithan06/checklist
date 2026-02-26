import os
import sys

# Ensure the current directory is in the path so 'backend' can be imported
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

from backend.wsgi import application

# Vercel's Python runtime expects 'app' or 'application'
app = application

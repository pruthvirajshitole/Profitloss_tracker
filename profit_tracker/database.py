"""
Database configuration for profit_tracker project.
Handles both development (SQLite) and production (PostgreSQL) environments.
"""

import os
from decouple import config

def get_database_config():
    """Get database configuration based on environment"""
    
    # Check if we're in production (Railway)
    if os.environ.get('RAILWAY_ENVIRONMENT') or os.environ.get('DATABASE_URL'):
        # Production: Use PostgreSQL from Railway
        return {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': config('DB_NAME', default=''),
                'USER': config('DB_USER', default=''),
                'PASSWORD': config('DB_PASSWORD', default=''),
                'HOST': config('DB_HOST', default=''),
                'PORT': config('DB_PORT', default='5432'),
                'OPTIONS': {
                    'sslmode': 'require',
                },
            }
        }
    else:
        # Development: Use SQLite
        return {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'db.sqlite3',
            }
        }

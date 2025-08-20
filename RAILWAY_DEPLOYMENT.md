# Deploying to Railway

This guide will help you deploy your Django Profit Tracker app to Railway.

## Prerequisites

1. **Railway Account**: Sign up at [railway.app](https://railway.app)
2. **Git Repository**: Your code should be in a Git repository (GitHub, GitLab, etc.)
3. **Railway CLI** (optional): Install with `npm install -g @railway/cli`

## Step-by-Step Deployment

### 1. Prepare Your Repository

Make sure all the configuration files are committed to your repository:
- `Procfile`
- `requirements.txt`
- `runtime.txt`
- `railway.json`
- `profit_tracker/production.py`
- `build.sh`

### 2. Connect to Railway

#### Option A: Via Web Interface (Recommended)
1. Go to [railway.app](https://railway.app) and sign in
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Choose your repository
5. Railway will automatically detect it's a Python app

#### Option B: Via CLI
```bash
# Login to Railway
railway login

# Initialize project
railway init

# Link to existing project
railway link
```

### 3. Set Environment Variables

In your Railway project dashboard, go to the "Variables" tab and add:

```
SECRET_KEY=your-very-secure-secret-key-here
DEBUG=False
RAILWAY_ENVIRONMENT=true
```

**Important**: Generate a new secret key for production:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### 4. Add PostgreSQL Database

1. In your Railway project, click "New Service"
2. Select "Database" → "PostgreSQL"
3. Railway will automatically provide a `DATABASE_URL` environment variable
4. This will be automatically used by your production settings

### 5. Deploy

1. Railway will automatically build and deploy when you push to your main branch
2. Or manually trigger a deployment from the dashboard
3. Monitor the build logs for any errors

### 6. Run Migrations

After deployment, you may need to run migrations:

```bash
# Via Railway CLI
railway run python manage.py migrate

# Or via Railway dashboard terminal
python manage.py migrate
```

### 7. Create Superuser (Optional)

```bash
railway run python manage.py createsuperuser
```

## Configuration Files Explained

### Procfile
Tells Railway to use Gunicorn as the WSGI server.

### requirements.txt
Lists all Python dependencies needed for production.

### runtime.txt
Specifies the Python version.

### railway.json
Railway-specific configuration for build and deployment.

### production.py
Production Django settings with security enhancements.

## Troubleshooting

### Common Issues

1. **Build Failures**: Check the build logs in Railway dashboard
2. **Database Connection**: Ensure `DATABASE_URL` is set correctly
3. **Static Files**: Verify `STATIC_ROOT` and whitenoise configuration
4. **Port Binding**: Railway uses `$PORT` environment variable

### Debug Mode

If you need to debug, temporarily set:
```
DEBUG=True
```

### Logs

View logs in Railway dashboard or via CLI:
```bash
railway logs
```

## Security Notes

- Never commit `.env` files with real secrets
- Use strong, unique secret keys
- Keep dependencies updated
- Enable HTTPS (Railway handles this automatically)

## Monitoring

Railway provides:
- Real-time logs
- Performance metrics
- Automatic scaling
- Health checks

## Next Steps

After successful deployment:
1. Set up custom domain (optional)
2. Configure monitoring and alerts
3. Set up CI/CD for automatic deployments
4. Consider adding a CDN for static files

## Support

- [Railway Documentation](https://docs.railway.app)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/)
- [Railway Discord](https://discord.gg/railway)

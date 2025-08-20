# MySQL Setup Guide for Profit & Loss Tracker

This guide will help you set up MySQL database for the Django Profit & Loss Tracker application.

## Prerequisites

- MySQL Server 8.0 or higher installed and running
- Python 3.8 or higher
- Access to MySQL command line or a MySQL client

## Step 1: Install MySQL Dependencies

```bash
python -m pip install -r requirements.txt
```

## Step 2: Create MySQL Database

### Option A: Using the Setup Script (Recommended)

1. Run the setup script:
   ```bash
   python setup_mysql.py
   ```

2. Choose option 1: "Create MySQL database"

3. Follow the prompts:
   - Enter MySQL host (default: localhost)
   - Enter MySQL port (default: 3306)
   - Enter MySQL username (default: root)
   - Enter MySQL password

4. The script will create the `profit_tracker` database automatically

### Option B: Manual MySQL Setup

1. Connect to MySQL:
   ```bash
   mysql -u root -p
   ```

2. Create the database:
   ```sql
   CREATE DATABASE profit_tracker CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

3. Verify the database was created:
   ```sql
   SHOW DATABASES;
   ```

4. Exit MySQL:
   ```sql
   EXIT;
   ```

## Step 3: Update Django Settings (if needed)

The default settings in `profit_tracker/settings.py` are:
- Database: `profit_tracker`
- User: `root`
- Password: (empty)
- Host: `localhost`
- Port: `3306`

If you need different credentials, edit the `DATABASES` section in `profit_tracker/settings.py`.

## Step 4: Run Django Migrations

```bash
python manage.py migrate
```

## Step 5: Create Superuser

```bash
python manage.py createsuperuser
```

## Step 6: Test the Application

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to verify everything is working.

## Troubleshooting

### Common MySQL Issues

1. **"Access denied for user"**
   - Check username and password
   - Ensure user has proper permissions
   - Try creating a new MySQL user with full privileges

2. **"Can't connect to MySQL server"**
   - Verify MySQL service is running
   - Check host and port settings
   - Ensure firewall allows connections

3. **"Unknown database"**
   - Run the setup script again
   - Check database name spelling
   - Verify database exists: `SHOW DATABASES;`

4. **Character set issues**
   - Ensure database uses `utf8mb4` character set
   - Check MySQL configuration for proper charset support

### Creating a New MySQL User (if needed)

```sql
-- Connect to MySQL as root
mysql -u root -p

-- Create new user
CREATE USER 'profit_user'@'localhost' IDENTIFIED BY 'your_password';

-- Grant privileges
GRANT ALL PRIVILEGES ON profit_tracker.* TO 'profit_user'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;

-- Exit
EXIT;
```

Then update `profit_tracker/settings.py` with the new credentials.

## Security Notes

- Change default MySQL root password
- Use strong passwords for production
- Limit user permissions to only necessary databases
- Consider using environment variables for sensitive data

## Support

If you encounter issues:
1. Check MySQL error logs
2. Verify Django settings
3. Test database connection manually
4. Ensure all dependencies are installed

---

**Happy tracking! 💰📊**

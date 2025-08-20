# Profit & Loss Tracker

A Django-based web application for tracking personal or business income and expenses with profit/loss calculations and timing information.

## Features

- **Dashboard Overview**: View total income, expenses, and net profit/loss at a glance
- **Transaction Management**: Add, edit, and delete income and expense entries
- **Color Coding**: 
  - 🟢 **Green** for income/profit amounts
  - 🔴 **Red** for expense/loss amounts
- **Timing Information**: Each transaction includes date and time stamps
- **Responsive Design**: Modern Bootstrap-based UI that works on all devices
- **Local Use**: Designed for personal/local use only

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Django 5.2 or higher
- MySQL Server 8.0 or higher
- MySQL client libraries

### Installation

1. **Clone or download the project files**

2. **Install dependencies**:
   ```bash
   python -m pip install -r requirements.txt
   ```

3. **Navigate to the project directory**:
   ```bash
   cd Profit
   ```

4. **Set up MySQL database**:
   - Make sure MySQL server is running
   - Run the setup script: `python setup_mysql.py`
   - Follow the prompts to create the database
   - Update `profit_tracker/settings.py` with your MySQL credentials if needed

5. **Run database migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser** (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Open your browser** and go to:
   ```
   http://127.0.0.1:8000/
   ```

## Usage

### Dashboard
- View summary of all income, expenses, and net profit/loss
- See recent transactions
- Quick access to add new transactions

### Adding Transactions
1. Click "Add Transaction" button
2. Select transaction type (Income or Expense)
3. Enter amount, description, and optional notes
4. Date and time are automatically set to current time
5. Click "Save Transaction"

### Managing Transactions
- **View All**: See complete transaction history with filtering options
- **Edit**: Modify existing transaction details
- **Delete**: Remove transactions with confirmation dialog

### Admin Panel
- Access at `http://127.0.0.1:8000/admin/`
- Use the superuser credentials you created
- Manage all transactions through Django admin interface

## File Structure

```
Profit/
├── manage.py                 # Django management script
├── profit_tracker/          # Main project settings
│   ├── settings.py         # Project configuration
│   ├── urls.py            # Main URL routing
│   └── wsgi.py            # WSGI configuration
├── transactions/           # Main app
│   ├── models.py          # Transaction data model
│   ├── views.py           # Business logic and views
│   ├── forms.py           # Form handling
│   ├── admin.py           # Admin interface configuration
│   ├── urls.py            # App-specific URL routing
│   └── templates/         # HTML templates
│       └── transactions/  # Template files
├── setup_mysql.py          # MySQL database setup script
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## MySQL Database Configuration

### Database Settings
The application is configured to use MySQL by default. The current settings in `profit_tracker/settings.py` are:
- **Database Engine**: MySQL
- **Database Name**: `profit_tracker`
- **Host**: `localhost`
- **Port**: `3306`
- **User**: `root`
- **Password**: (empty by default)

### Updating Database Credentials
If you need to change the database connection details:
1. Edit `profit_tracker/settings.py`
2. Update the `DATABASES` configuration
3. Restart the Django development server

### MySQL Server Requirements
- MySQL Server 8.0 or higher
- UTF8MB4 character set support
- Proper user permissions for the database

## Customization

### Changing Currency Symbol
To change from ₹ (Rupee) to another currency:
1. Edit the templates in `transactions/templates/transactions/`
2. Replace all instances of `₹` with your preferred currency symbol

### Adding New Fields
To add new transaction fields:
1. Modify `transactions/models.py`
2. Update `transactions/forms.py`
3. Modify the templates
4. Run `python manage.py makemigrations` and `python manage.py migrate`

## Security Notes

- This application is designed for **local use only**
- Do not deploy to public servers without proper security measures
- The default Django development server is not suitable for production use

## Troubleshooting

### Common Issues

1. **"No module named 'django'"**
   - Install dependencies: `python -m pip install -r requirements.txt`

2. **MySQL connection errors**
   - Ensure MySQL server is running
   - Check database credentials in `profit_tracker/settings.py`
   - Verify database exists: `python setup_mysql.py`
   - Install MySQL client: `python -m pip install mysqlclient`

3. **Database migration errors**
   - Run migrations: `python manage.py migrate`
   - If switching from SQLite, you may need to start fresh

4. **Template errors**
   - Ensure all template files are in the correct directory structure

5. **Port already in use**
   - Use a different port: `python manage.py runserver 8001`

## Support

For local development and personal use. The application includes comprehensive error handling and user-friendly messages to guide you through any issues.

---

**Enjoy tracking your profits and losses! 💰📊**

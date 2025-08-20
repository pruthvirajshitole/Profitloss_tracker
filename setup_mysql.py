#!/usr/bin/env python3
"""
MySQL Database Setup Script for Profit & Loss Tracker

This script helps you set up the MySQL database for the Django application.
Make sure you have MySQL server running and have the necessary permissions.
"""

import mysql.connector
from mysql.connector import Error
import getpass

def create_database():
    """Create the MySQL database for the profit tracker application"""
    
    print("🚀 MySQL Database Setup for Profit & Loss Tracker")
    print("=" * 50)
    
    # Get database connection details
    host = input("Enter MySQL host (default: localhost): ").strip() or "localhost"
    port = input("Enter MySQL port (default: 3306): ").strip() or "3306"
    user = input("Enter MySQL username (default: root): ").strip() or "root"
    password = getpass.getpass("Enter MySQL password: ")
    
    try:
        # Connect to MySQL server
        print(f"\n🔌 Connecting to MySQL server at {host}:{port}...")
        connection = mysql.connector.connect(
            host=host,
            port=int(port),
            user=user,
            password=password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database
            database_name = "profit_tracker"
            print(f"\n📊 Creating database '{database_name}'...")
            
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
            print(f"✅ Database '{database_name}' created successfully!")
            
            # Test connection to the new database
            cursor.execute(f"USE {database_name}")
            print(f"✅ Successfully connected to database '{database_name}'")
            
            # Show database info
            cursor.execute("SELECT VERSION()")
            version = cursor.fetchone()
            print(f"📋 MySQL Version: {version[0]}")
            
            print(f"\n🎉 Database setup completed successfully!")
            print(f"📝 Update your Django settings with these credentials:")
            print(f"   - Database Name: {database_name}")
            print(f"   - Username: {user}")
            print(f"   - Password: {password}")
            print(f"   - Host: {host}")
            print(f"   - Port: {port}")
            
            return True
            
    except Error as e:
        print(f"❌ Error: {e}")
        return False
        
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("\n🔌 Database connection closed.")

def test_connection():
    """Test the database connection with current Django settings"""
    
    print("\n🧪 Testing Django Database Connection...")
    print("=" * 50)
    
    try:
        import os
        import django
        
        # Set up Django environment
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'profit_tracker.settings')
        django.setup()
        
        from django.db import connection
        cursor = connection.cursor()
        
        # Test a simple query
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        
        if result and result[0] == 1:
            print("✅ Django database connection successful!")
            return True
        else:
            print("❌ Django database connection failed!")
            return False
            
    except Exception as e:
        print(f"❌ Error testing Django connection: {e}")
        return False

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Create MySQL database")
    print("2. Test Django database connection")
    print("3. Both")
    
    choice = input("\nEnter your choice (1, 2, or 3): ").strip()
    
    if choice == "1":
        create_database()
    elif choice == "2":
        test_connection()
    elif choice == "3":
        if create_database():
            test_connection()
    else:
        print("Invalid choice. Please run the script again.")

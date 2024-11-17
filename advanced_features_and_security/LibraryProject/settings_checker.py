import os

def check_settings(file_path):
    # Define required settings
    required_settings = [
        "SECURE_BROWSER_XSS_FILTER",
        "X_FRAME_OPTIONS",
        "SECURE_CONTENT_TYPE_NOSNIFF",
        "CSRF_COOKIE_SECURE",
        "SESSION_COOKIE_SECURE",
    ]
    missing_settings = []

    try:
        # Read the settings.py file
        with open(file_path, 'r') as file:
            settings_content = file.read()

        # Check for each required setting
        for setting in required_settings:
            if setting not in settings_content:
                missing_settings.append(setting)

        # Output the result
        if missing_settings:
            print("Missing required settings:")
            for setting in missing_settings:
                print(f" - {setting}")
        else:
            print("All required settings are present!")

    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Path to the settings.py file
project_root = os.path.dirname(os.path.abspath(__file__))
settings_file_path = os.path.join(project_root, 'LibraryProject', 'LibraryProject', 'settings.py')

# Run the checker
check_settings(settings_file_path)

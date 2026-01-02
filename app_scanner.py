import os
import json

def scan_installed_apps(save_path="installed_apps.json"):
    scan_paths = [
        "C:\\Program Files",
        "C:\\Program Files (x86)",
        os.path.expanduser("~\\AppData\\Local\\Programs")
    ]

    apps = []

    for base_path in scan_paths:
        for root, dirs, files in os.walk(base_path):
            for file in files:
                if file.lower().endswith(".exe"):
                    apps.append({
                        "name": file,
                        "path": os.path.join(root, file)
                    })

    # Remove duplicates
    seen = set()
    unique_apps = []
    for app in apps:
        key = app["path"].lower()
        if key not in seen:
            unique_apps.append(app)
            seen.add(key)

    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(unique_apps, f, indent=4)

    print(f"✅ Scanned {len(unique_apps)} apps.")
    return unique_apps


def find_app_path(app_name, app_db="installed_apps.json"):
    try:
        if not os.path.exists(app_db):
            print("📦 No app list found. Scanning now...")
            scan_installed_apps(app_db)

        with open(app_db, "r", encoding="utf-8") as f:
            apps = json.load(f)

        app_name_lower = app_name.lower()
        for app in apps:
            if app_name_lower in app["name"].lower():
                name = app["name"].replace(".exe", "")
                return f"{name} is installed at {app['path']}"

        return f"I couldn't find {app_name} in the installed apps."
    except:
        return "Something went wrong while searching for the app."

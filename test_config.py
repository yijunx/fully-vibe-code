#!/usr/bin/env python3
"""Test script to verify configuration loading."""

from app.utils.config import settings

def main():
    print("Configuration loaded successfully!")
    print(f"Environment: {settings.env}")
    print(f"Namespace: {settings.namespace}")
    print(f"Service Name: {settings.service_name}")
    print(f"Service Version: {settings.service_version}")
    print(f"Database URI: {settings.database_uri}")
    print(f"Argo URL: {settings.argo_url}")
    print(f"Database URL (property): {settings.database_url}")

if __name__ == "__main__":
    main() 
import requests
import time
import subprocess
import sys

def test_server():
    print("Starting server...")
    # Start server in background
    process = subprocess.Popen(["venv/bin/python", "server.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(5) # Wait for startup

    url = "http://localhost:5001/api/convert"
    payload = {"java_code": "System.out.println(\"Server Test\");"}

    print(f"Testing {url}...")
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print("\n✅ Server Response:")
        print(response.json())
    except Exception as e:
        print(f"\n❌ Server Test Failed: {e}")
    finally:
        print("Stopping server...")
        process.terminate()

if __name__ == "__main__":
    test_server()

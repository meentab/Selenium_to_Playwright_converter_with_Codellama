import requests
import json
import sys

def test_ollama():
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "codellama",
        "prompt": "Write a one-line Java Hello World system out print.",
        "stream": False
    }
    
    print(f"Connecting to {url} with model 'codellama'...")
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        result = response.json()
        print("\n✅ Success! Response:")
        print(result.get("response", "No response key found"))
        return 0
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Could not connect to Ollama. Is it running on port 11434?")
        return 1
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(test_ollama())

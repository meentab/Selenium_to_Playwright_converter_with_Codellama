import requests
import json
import os

class OllamaClient:
    def __init__(self, model="codellama", host="http://localhost:11434"):
        self.model = model
        self.host = host
        self.api_url = f"{host}/api/generate"
        self.system_prompt = self._load_system_prompt()

    def _load_system_prompt(self):
        """Loads the system prompt from architecture/prompt_engineering.md"""
        try:
            # Go up one level from tools/ to project root, then to architecture/
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            prompt_path = os.path.join(base_dir, "architecture", "prompt_engineering.md")
            
            with open(prompt_path, "r") as f:
                content = f.read()
                # Basic parsing to extract the prompts (in a real scenario, might want more robust parsing)
                return content
        except Exception as e:
            print(f"Warning: Could not load system prompt: {e}")
            return "You are a code converter."

    def convert(self, java_code):
        """Sends Java code to Ollama and returns TypeScript."""
        
        full_prompt = f"""
{self.system_prompt}

---

**Java Code to Convert:**
```java
{java_code}
```

**TypeScript Output:**
"""
        payload = {
            "model": self.model,
            "prompt": full_prompt,
            "stream": False,
             "options": {
                "temperature": 0.2  # Low temperature for deterministic code
            }
        }

        try:
            response = requests.post(self.api_url, json=payload, timeout=60)
            response.raise_for_status()
            result = response.json()
            return result.get("response", "").strip()
        except requests.exceptions.RequestException as e:
            return f"Error: Failed to connect to Ollama: {e}"

if __name__ == "__main__":
    # Quick functional test
    client = OllamaClient()
    print("System Prompt Loaded:", len(client.system_prompt), "chars")
    print("Testing conversion...")
    print(client.convert("System.out.println(\"Test\");"))

# 🚀 B.L.A.S.T. Converter
**Selenium Java to Playwright TypeScript Converter**

This tool leverages a local LLM (**Ollama/CodeLlama**) to intelligently convert legacy Selenium Java (TestNG) code into modern Playwright TypeScript code. It features a stunning "Glassmorphism" UI and handles file management for you.

## ✨ Features
- **AI-Powered Conversion:** Understands intent (e.g., `driver.get` → `page.goto`) rather than just regex replacement.
- **Modern UI:** A clean, dark-mode interface with real-time syntax highlighting.
- **Local & Private:** Runs entirely on your machine using Ollama. No data leaves your network.
- **Save to Disk:** Instantly save converted files to an `output/` directory.

## 🛠️ Prerequisites

1.  **Python 3.10+**
2.  **Ollama** (for the local LLM)
    -   [Download Ollama](https://ollama.com)
    -   Pull the model:
        ```bash
        ollama run codellama
        ```
    -   *Ensure Ollama is running on port 11434.*

## 🚀 Setup & Usage

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/meentab/Selenium_to_Playwright_converter_with_Codellama.git
    cd Selenium_to_Playwright_converter_with_Codellama
    ```

2.  **Start the Application**
    We have provided a convenient startup script:
    ```bash
    chmod +x blast_off.sh
    ./blast_off.sh
    ```
    *This script automatically sets up a Python virtual environment (`venv`), installs dependencies (`flask`, `requests`), and launches the server.*

3.  **Access the UI**
    Open your browser to: [http://localhost:5001](http://localhost:5001)

## 📖 How to Use

1.  Paste your **Selenium Java** code into the left pane.
2.  Click **⚡ Convert**.
3.  Wait for the AI to generate the **Playwright TypeScript** code in the right pane.
4.  Click **💾 Save to Disk** to save the result to the `output/` folder.

## 📂 Project Structure

-   `server.py` - Flask Backend handling API requests.
-   `tools/llm_client.py` - Wrapper for communicating with Ollama.
-   `ui/` - Frontend assets (HTML, CSS, JS).
-   `blast_off.sh` - One-click launch script.
-   `output/` - Directory where converted files are saved.

---
*Powered by B.L.A.S.T. Protocol (Blueprint, Link, Architect, Stylize, Trigger)*

#!/bin/bash
# blast_off.sh

echo "🚀 B.L.A.S.T. Converter Initiation..."
echo "Checking dependencies..."

if [ ! -d "venv" ]; then
    echo "⚠️ venv not found. Creating..."
    python3 -m venv venv
    venv/bin/pip install -r requirements.txt
else 
    echo "✅ venv found."
fi

# Ensure requirements exist
if [ ! -f "requirements.txt" ]; then
    echo "flask
requests" > requirements.txt
    venv/bin/pip install -r requirements.txt
fi

echo "✨ Launching Server..."
echo "🌍 Open your browser to: http://localhost:5001"
echo "-----------------------------------------------"
venv/bin/python server.py

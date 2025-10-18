#!/bin/bash

# MuseScore MCP Startup Script
# Starts the WebSocket bridge and Python MCP server

echo "🎵 MuseScore MCP System Starting..."
echo ""

# Get project directory
PROJECT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"

echo "📁 Project: $PROJECT_DIR"
echo ""

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "✗ Error: Python 3 not found!"
    echo "  Please install Python 3.8+"
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "🐍 Python version: $PYTHON_VERSION"

# Navigate to project
cd "$PROJECT_DIR" || exit 1

# Check if venv exists
if [ ! -d ".venv" ]; then
    echo ""
    echo "📦 Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate venv
echo "✓ Activating virtual environment..."
source .venv/bin/activate

# Check if requirements are installed
echo "📋 Checking dependencies..."
if ! pip show mcp &> /dev/null; then
    echo "  Installing dependencies..."
    pip install --upgrade pip > /dev/null 2>&1
    pip install -r requirements.txt
fi

echo ""
echo "="*60
echo "✓ Environment ready!"
echo "="*60
echo ""
echo "⚠️  IMPORTANT NEXT STEPS:"
echo ""
echo "1. Open MuseScore 4.x (in another window)"
echo "   Command: musescore4"
echo ""
echo "2. Create a new score or open an existing one"
echo "   File → New"
echo ""
echo "3. Enable the WebSocket plugin:"
echo "   Plugins → MuseScore API Server"
echo ""
echo "4. Keep this terminal open"
echo ""
echo "5. Open ANOTHER terminal and run:"
echo "   cd $PROJECT_DIR"
echo "   source .venv/bin/activate"
echo "   python3 examples/01_simple_melody.py"
echo ""
echo "="*60
echo ""
echo "Starting MCP server on ws://localhost:8765..."
echo ""

# Start the server
python3 server.py

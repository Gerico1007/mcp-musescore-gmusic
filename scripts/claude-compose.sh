#!/bin/bash

# Claude Code MuseScore Composition Launcher
# Starts Claude Code with MuseScore MCP pre-configured

echo "🎵 Launching Claude Code with MuseScore MCP..."
echo ""

# Get project directory
PROJECT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"

# Check if MCP server is running
echo "Checking MuseScore MCP server..."

# Try to connect to WebSocket
nc -z localhost 8765 2>/dev/null
if [ $? -eq 0 ]; then
    echo "✓ MuseScore MCP server is running on port 8765"
else
    echo "⚠️  MuseScore MCP server not detected on port 8765"
    echo "   Make sure:"
    echo "   1. MuseScore is open"
    echo "   2. Plugin is running: Plugins → MuseScore API Server"
    echo "   3. Python server started: python3 server.py"
    echo ""
    echo "Starting MCP server in background..."
    cd "$PROJECT_DIR"
    source .venv/bin/activate
    python3 server.py > /tmp/musescore-mcp.log 2>&1 &
    MCP_PID=$!
    echo "   Server PID: $MCP_PID"
    sleep 2
fi

echo ""
echo "🚀 Starting Claude Code with MuseScore MCP enabled..."
echo ""
echo "Available commands:"
echo "  • add_note() - Add a note to the score"
echo "  • add_rest() - Add a rest"
echo "  • go_to_beginning_of_score() - Jump to start"
echo "  • next_staff() - Move to next staff"
echo "  • getScore() - Get score information"
echo "  • And 25+ more composition tools!"
echo ""
echo "Example: 'Compose a C Major scale'"
echo ""
echo "MuseScore MCP is already registered!"
echo "Just start Claude Code normally:"
echo ""

# Launch Claude Code
# MCP server is pre-configured via 'claude mcp add'
claude

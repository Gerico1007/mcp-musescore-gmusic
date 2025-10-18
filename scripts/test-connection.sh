#!/bin/bash

# Test MuseScore MCP Connection
# Verifies connection to MuseScore WebSocket server

echo "🔍 Testing MuseScore MCP Connection..."
echo ""

# Get project directory
PROJECT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"

# Navigate to project
cd "$PROJECT_DIR" || exit 1

# Activate venv
if [ ! -d ".venv" ]; then
    echo "✗ Error: Virtual environment not found!"
    echo "  Run: python3 -m venv .venv"
    exit 1
fi

source .venv/bin/activate

# Test connection using Python
python3 << 'EOF'
import asyncio
import websockets
import json
import sys

async def test_connection():
    uri = "ws://localhost:8765"

    try:
        print(f"Connecting to {uri}...")
        async with websockets.connect(uri, timeout=5) as ws:
            print("✓ Connected!")
            print("")

            # Test ping
            print("Sending ping...")
            await ws.send(json.dumps({"action": "ping", "params": {}}))
            response = await ws.recv()
            result = json.loads(response)

            print(f"Response: {result}")

            if result.get("status") == "success":
                print("✓ Ping successful!")
                print("")
                print("🎵 MuseScore MCP is ready to compose!")
                return 0
            else:
                print("✗ Unexpected response")
                return 1

    except ConnectionRefusedError:
        print("✗ Connection refused!")
        print("")
        print("Make sure:")
        print("  1. MuseScore is running")
        print("  2. Plugin is enabled: Plugins → MuseScore API Server")
        print("  3. Python MCP server is running: python3 server.py")
        return 1
    except asyncio.TimeoutError:
        print("✗ Connection timeout!")
        print("")
        print("WebSocket server not responding on port 8765")
        print("Make sure: Plugins → MuseScore API Server is running")
        return 1
    except Exception as e:
        print(f"✗ Error: {e}")
        return 1

result = asyncio.run(test_connection())
sys.exit(result)
EOF

exit $?

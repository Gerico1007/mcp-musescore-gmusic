#!/usr/bin/env python3
"""
Test Script: Full Composition Workflow
Demonstrates Claude Code composing music in MuseScore

This script creates "Twinkle Twinkle Little Star" in MuseScore
"""

import asyncio
import json
import websockets
from typing import Any

class MuseScoreMCPClient:
    """Simple WebSocket client for MuseScore MCP"""

    def __init__(self, uri: str = "ws://localhost:8765"):
        self.uri = uri
        self.websocket = None

    async def connect(self):
        """Connect to MuseScore WebSocket server"""
        self.websocket = await websockets.connect(self.uri)
        print(f"✓ Connected to MuseScore at {self.uri}")

    async def send_command(self, action: str, params: dict = None) -> Any:
        """Send a command to MuseScore and get response"""
        if params is None:
            params = {}

        command = {
            "action": action,
            "params": params
        }

        print(f"  📝 {action}", end="")

        await self.websocket.send(json.dumps(command))
        response = await self.websocket.recv()
        result = json.loads(response)

        if result.get("status") == "success":
            print(" ✓")
        else:
            print(f" ✗ Error: {result.get('message', 'Unknown error')}")

        return result

    async def close(self):
        """Close connection"""
        if self.websocket:
            await self.websocket.close()


async def compose_twinkle():
    """Compose 'Twinkle Twinkle Little Star' in MuseScore"""

    client = MuseScoreMCPClient()

    try:
        print("\n" + "="*60)
        print("🎵 MuseScore MCP Full Composition Workflow Test")
        print("="*60)

        # Step 1: Connect
        print("\n[STEP 1] Connecting to MuseScore...")
        await client.connect()

        # Step 2: Test connection
        print("\n[STEP 2] Testing connection with ping...")
        response = await client.send_command("ping")
        print(f"  Response: {response.get('result')}")

        # Step 3: Set up score
        print("\n[STEP 3] Setting up score...")
        await client.send_command("setTitle", {"title": "Twinkle Twinkle Little Star"})
        await client.send_command("goToBeginningOfScore")

        # Step 4: Compose the melody
        print("\n[STEP 4] Composing melody...")
        print("  (Twinkle Twinkle Little Star - C Major, 4/4 time)")

        # MIDI pitch notes: C=60, D=62, E=64, F=65, G=67, A=69, B=71
        # Twinkle notes: C C G G A A G (first phrase)
        melody = [
            (60, "C"),    # Twin
            (60, "C"),    # kle
            (67, "G"),    # Twin
            (67, "G"),    # kle
            (69, "A"),    # Lit
            (69, "A"),    # tle
            (67, "G"),    # Star
            (65, "F"),    # up
            (64, "E"),    # a
            (64, "E"),    # bove
            (62, "D"),    # the
            (62, "D"),    # world
            (60, "C"),    # so
            (60, "C"),    # high
        ]

        # Add notes with quarter note duration
        quarter_note = {"numerator": 1, "denominator": 4}

        for pitch, note_name in melody:
            await client.send_command("addNote", {
                "pitch": pitch,
                "duration": quarter_note,
                "advanceCursorAfterAction": True
            })

        print(f"\n  ✓ Added {len(melody)} notes to the score!")

        # Step 5: Add lyrics
        print("\n[STEP 5] Adding lyrics...")
        lyrics = [
            "Twin", "kle", "Twin", "kle", "Lit", "tle", "Star",
            "up", "a", "bove", "the", "world", "so", "high"
        ]

        await client.send_command("goToBeginningOfScore")

        for lyric in lyrics:
            await client.send_command("addLyricsToCurrentNote", {"text": lyric})
            await client.send_command("nextElement")

        print(f"  ✓ Added {len(lyrics)} lyrics!")

        # Step 6: Get score info
        print("\n[STEP 6] Retrieving score information...")
        score_info = await client.send_command("getScore")

        # Step 7: Return to beginning
        print("\n[STEP 7] Returning to beginning of score...")
        await client.send_command("goToBeginningOfScore")

        print("\n" + "="*60)
        print("✨ COMPOSITION COMPLETE! ✨")
        print("="*60)
        print("\n✓ The melody 'Twinkle Twinkle Little Star' has been")
        print("  composed in MuseScore with lyrics!")
        print("\nCheck your MuseScore window - the music is now there!")
        print("\nYou can:")
        print("  • Play it back (spacebar in MuseScore)")
        print("  • Export it as PDF, MusicXML, or audio")
        print("  • Further edit it in MuseScore")
        print("\n" + "="*60 + "\n")

    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()

    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(compose_twinkle())

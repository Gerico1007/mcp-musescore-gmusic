#!/usr/bin/env python3
"""
Example 5: Full Song Composition
Demonstrates complete song structure
Composes: Verse-Chorus-Verse-Chorus structure
"""

import asyncio
import json
import websockets


async def compose_full_song():
    """Compose a complete song with structure"""

    uri = "ws://localhost:8765"

    try:
        async with websockets.connect(uri) as ws:
            print("\n🎵 Example 5: Full Song - Verse-Chorus Structure\n")

            quarter = {"numerator": 1, "denominator": 4}
            half = {"numerator": 1, "denominator": 2}

            # Go to beginning
            print("Setting up score...")
            await ws.send(json.dumps({
                "action": "goToBeginningOfScore",
                "params": {}
            }))
            await ws.recv()

            # Song structure
            sections = [
                {
                    "name": "Verse 1",
                    "melody": [60, 62, 64, 65, 67, 69, 71, 72],
                    "durations": [quarter] * 8,
                },
                {
                    "name": "Chorus",
                    "melody": [72, 71, 69, 67, 65, 64, 62, 60],
                    "durations": [half] * 4,
                },
                {
                    "name": "Verse 2",
                    "melody": [60, 62, 64, 65, 67, 69, 71, 72],
                    "durations": [quarter] * 8,
                },
                {
                    "name": "Chorus",
                    "melody": [72, 71, 69, 67, 65, 64, 62, 60],
                    "durations": [half] * 4,
                },
                {
                    "name": "Bridge",
                    "melody": [65, 67, 69, 71, 72, 71, 69, 67],
                    "durations": [quarter] * 8,
                },
                {
                    "name": "Final Chorus",
                    "melody": [72, 71, 69, 67, 65, 64, 62, 60],
                    "durations": [half] * 4,
                },
            ]

            # Compose song
            print("Composing full song...\n")

            total_notes = 0
            for section in sections:
                print(f"  [{section['name']}]")

                for pitch, duration in zip(section['melody'], section['durations']):
                    await ws.send(json.dumps({
                        "action": "addNote",
                        "params": {
                            "pitch": pitch,
                            "duration": duration,
                            "advanceCursorAfterAction": True
                        }
                    }))
                    await ws.recv()
                    total_notes += 1

                # Add measure for visual separation
                try:
                    await ws.send(json.dumps({
                        "action": "appendMeasure",
                        "params": {"count": 1}
                    }))
                    await ws.recv()
                except:
                    pass  # Measure append might not be supported

                print(f"    ✓ {len(section['melody'])} notes added\n")

            # Return to beginning
            print("Returning to beginning...")
            await ws.send(json.dumps({
                "action": "goToBeginningOfScore",
                "params": {}
            }))
            await ws.recv()

            print("\n✓ Full song complete!")
            print(f"  Total: {total_notes} notes")
            print("  Structure:")
            print("    - Verse 1 (8 quarter notes)")
            print("    - Chorus (4 half notes)")
            print("    - Verse 2 (8 quarter notes)")
            print("    - Chorus (4 half notes)")
            print("    - Bridge (8 quarter notes)")
            print("    - Final Chorus (4 half notes)")
            print("  Play in MuseScore: Press spacebar\n")

    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(compose_full_song())

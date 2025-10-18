#!/usr/bin/env python3
"""
Example 3: Multi-Staff Composition
Demonstrates composing on multiple staves
Composes: Simple four-part harmony (SATB-like)
"""

import asyncio
import json
import websockets


async def compose_multi_staff():
    """Compose on multiple staves"""

    uri = "ws://localhost:8765"

    try:
        async with websockets.connect(uri) as ws:
            print("\n🎵 Example 3: Multi-Staff Composition - Four Staves\n")

            quarter_note = {"numerator": 1, "denominator": 4}

            # Go to beginning
            print("Setting up score...")
            await ws.send(json.dumps({
                "action": "goToBeginningOfScore",
                "params": {}
            }))
            await ws.recv()

            # Define four melodies for different staves
            staves = [
                ([72, 71, 69, 67], "Staff 1 (High)"),    # High voice
                ([67, 65, 64, 62], "Staff 2 (Mid-High)"), # Mid-high voice
                ([55, 53, 52, 50], "Staff 3 (Mid-Low)"),  # Mid-low voice
                ([48, 46, 45, 43], "Staff 4 (Low)"),      # Low voice
            ]

            # Compose on each staff
            for staff_num, (pitches, staff_name) in enumerate(staves):
                print(f"\n  Composing {staff_name}...")

                for pitch in pitches:
                    print(f"    MIDI {pitch}...", end=" ")
                    await ws.send(json.dumps({
                        "action": "addNote",
                        "params": {
                            "pitch": pitch,
                            "duration": quarter_note,
                            "advanceCursorAfterAction": True
                        }
                    }))
                    await ws.recv()
                    print("✓")

                # Move to next staff (if not last)
                if staff_num < len(staves) - 1:
                    print(f"\n  Moving to next staff...")
                    await ws.send(json.dumps({
                        "action": "nextStaff",
                        "params": {}
                    }))
                    await ws.recv()

            # Return to beginning
            print("\nReturning to beginning...")
            await ws.send(json.dumps({
                "action": "goToBeginningOfScore",
                "params": {}
            }))
            await ws.recv()

            print("\n✓ Multi-staff composition complete!")
            print("  Four different melodies on four staves")
            print("  Play in MuseScore: Press spacebar\n")

    except Exception as e:
        print(f"✗ Error: {e}")


if __name__ == "__main__":
    asyncio.run(compose_multi_staff())

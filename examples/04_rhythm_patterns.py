#!/usr/bin/env python3
"""
Example 4: Rhythm Patterns
Demonstrates complex rhythmic patterns
Composes: Various note durations and rhythms
"""

import asyncio
import json
import websockets


async def compose_rhythm_patterns():
    """Compose with different rhythmic patterns"""

    uri = "ws://localhost:8765"

    try:
        async with websockets.connect(uri) as ws:
            print("\n🎵 Example 4: Rhythm Patterns - Various Durations\n")

            # Go to beginning
            print("Setting up score...")
            await ws.send(json.dumps({
                "action": "goToBeginningOfScore",
                "params": {}
            }))
            await ws.recv()

            # Different rhythm patterns
            patterns = [
                {
                    "name": "Whole Notes",
                    "notes": [
                        (60, {"numerator": 1, "denominator": 1}),  # Whole
                    ]
                },
                {
                    "name": "Half Notes",
                    "notes": [
                        (62, {"numerator": 1, "denominator": 2}),  # Half
                        (64, {"numerator": 1, "denominator": 2}),  # Half
                    ]
                },
                {
                    "name": "Quarter Notes",
                    "notes": [
                        (65, {"numerator": 1, "denominator": 4}),  # Q
                        (67, {"numerator": 1, "denominator": 4}),  # Q
                        (69, {"numerator": 1, "denominator": 4}),  # Q
                        (71, {"numerator": 1, "denominator": 4}),  # Q
                    ]
                },
                {
                    "name": "Eighth Notes",
                    "notes": [
                        (72, {"numerator": 1, "denominator": 8}),  # E
                        (71, {"numerator": 1, "denominator": 8}),  # E
                        (69, {"numerator": 1, "denominator": 8}),  # E
                        (67, {"numerator": 1, "denominator": 8}),  # E
                        (65, {"numerator": 1, "denominator": 8}),  # E
                        (64, {"numerator": 1, "denominator": 8}),  # E
                        (62, {"numerator": 1, "denominator": 8}),  # E
                        (60, {"numerator": 1, "denominator": 8}),  # E
                    ]
                },
                {
                    "name": "Mixed Rhythm",
                    "notes": [
                        (60, {"numerator": 1, "denominator": 4}),  # Q
                        (62, {"numerator": 1, "denominator": 4}),  # Q
                        (64, {"numerator": 1, "denominator": 8}),  # E
                        (65, {"numerator": 1, "denominator": 8}),  # E
                        (67, {"numerator": 1, "denominator": 2}),  # Half
                    ]
                },
                {
                    "name": "Dotted Rhythm",
                    "notes": [
                        (69, {"numerator": 3, "denominator": 8}),  # Dotted Q
                        (71, {"numerator": 1, "denominator": 8}),  # E
                        (72, {"numerator": 1, "denominator": 2}),  # Half
                    ]
                },
            ]

            print("Composing rhythm patterns...\n")

            for pattern in patterns:
                print(f"  {pattern['name']}:")

                for pitch, duration in pattern['notes']:
                    duration_name = {
                        (1, 1): "W",
                        (1, 2): "H",
                        (1, 4): "Q",
                        (1, 8): "E",
                        (1, 16): "S",
                        (3, 8): "DQ",
                        (3, 4): "DH",
                    }.get((duration["numerator"], duration["denominator"]), "?")

                    print(f"    MIDI {pitch} ({duration_name})...", end=" ")

                    await ws.send(json.dumps({
                        "action": "addNote",
                        "params": {
                            "pitch": pitch,
                            "duration": duration,
                            "advanceCursorAfterAction": True
                        }
                    }))
                    await ws.recv()
                    print("✓")

                print()

            # Return to beginning
            print("Returning to beginning...")
            await ws.send(json.dumps({
                "action": "goToBeginningOfScore",
                "params": {}
            }))
            await ws.recv()

            print("\n✓ Rhythm patterns complete!")
            print("  W=Whole, H=Half, Q=Quarter, E=Eighth, S=Sixteenth")
            print("  DQ=Dotted Quarter, DH=Dotted Half")
            print("  Play in MuseScore: Press spacebar\n")

    except Exception as e:
        print(f"✗ Error: {e}")


if __name__ == "__main__":
    asyncio.run(compose_rhythm_patterns())

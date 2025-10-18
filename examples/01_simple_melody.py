#!/usr/bin/env python3
"""
Example 1: Simple Melody
Demonstrates basic note composition
Composes: C Major Scale ascending
"""

import asyncio
import json
import websockets


async def compose_c_major_scale():
    """Compose a simple C major scale"""

    uri = "ws://localhost:8765"

    try:
        async with websockets.connect(uri) as ws:
            print("\n🎵 Example 1: Simple Melody - C Major Scale\n")

            # C Major Scale: C D E F G A B C
            # MIDI: 60=C, 62=D, 64=E, 65=F, 67=G, 69=A, 71=B, 72=C
            pitches = [60, 62, 64, 65, 67, 69, 71, 72]
            quarter_note = {"numerator": 1, "denominator": 4}

            # Go to beginning
            print("Setting up score...")
            await ws.send(json.dumps({
                "action": "goToBeginningOfScore",
                "params": {}
            }))
            response = await ws.recv()
            print(response)

            # Add notes
            print("\nComposing C Major Scale...")
            note_names = ["C", "D", "E", "F", "G", "A", "B", "C"]

            for pitch, name in zip(pitches, note_names):
                print(f"  Adding {name} (MIDI {pitch})...", end=" ")
                await ws.send(json.dumps({
                    "action": "addNote",
                    "params": {
                        "pitch": pitch,
                        "duration": quarter_note,
                        "advanceCursorAfterAction": True
                    }
                }))
                response = await ws.recv()
                print("✓")

            # Return to beginning
            print("\nReturning to beginning...")
            await ws.send(json.dumps({
                "action": "goToBeginningOfScore",
                "params": {}
            }))
            await ws.recv()

            print("\n✓ Composition complete!")
            print("  Play in MuseScore: Press spacebar")
            print("  Export as PDF: File → Export → PDF\n")

    except Exception as e:
        print(f"✗ Error: {e}")


if __name__ == "__main__":
    asyncio.run(compose_c_major_scale())

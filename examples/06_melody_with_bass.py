#!/usr/bin/env python3
"""
Example 6: Melody with Bass Line
Demonstrates composing melody and bass together
Creates: Two-part composition (melody on top, bass below)
"""

import asyncio
import json
import websockets


async def compose_melody_with_bass():
    """Compose a melody with complementary bass line"""

    uri = "ws://localhost:8765"

    try:
        async with websockets.connect(uri) as ws:
            print("\n🎵 Example 6: Melody with Bass Line\n")

            quarter = {"numerator": 1, "denominator": 4}
            half = {"numerator": 1, "denominator": 2}

            # Go to beginning
            print("Setting up score...")
            await ws.send(json.dumps({
                "action": "goToBeginningOfScore",
                "params": {}
            }))
            await ws.recv()

            # ===== MELODY (First Staff) =====
            print("\n[MELODY] Composing upper voice...")

            # Melody: C Major scale with rhythm variation
            melody = [
                (60, quarter, "C"),
                (60, quarter, "C"),
                (62, quarter, "D"),
                (64, half, "E"),
                (65, quarter, "F"),
                (67, quarter, "G"),
                (69, half, "A"),
                (71, quarter, "B"),
                (72, quarter, "C"),
            ]

            total_notes = 0

            for pitch, duration, note_name in melody:
                print(f"  Melody: {note_name} (MIDI {pitch})...", end=" ")
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
                total_notes += 1

            # ===== BASS LINE (Second Staff) =====
            print("\n[BASS] Moving to bass staff...")
            await ws.send(json.dumps({
                "action": "nextStaff",
                "params": {}
            }))
            await ws.recv()

            print("Composing bass line...")

            # Bass line: Harmonic foundation (lower octave, supporting chords)
            # Follows chord structure: I-I-I-IV-IV-V-V-I-I
            bass = [
                (48, half, "C"),       # C (root of I chord) - 2 beats
                (48, quarter, "C"),    # C (root of I chord)
                (50, quarter, "D"),    # D (third)
                (53, half, "F"),       # F (root of IV chord)
                (53, quarter, "F"),    # F (root of IV chord)
                (55, quarter, "G"),    # G (third)
                (55, half, "G"),       # G (root of V chord)
                (48, quarter, "C"),    # C (root of I chord)
                (48, quarter, "C"),    # C (final)
            ]

            for pitch, duration, note_name in bass:
                print(f"  Bass: {note_name} (MIDI {pitch})...", end=" ")
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
                total_notes += 1

            # Return to beginning
            print("\nReturning to beginning...")
            await ws.send(json.dumps({
                "action": "goToBeginningOfScore",
                "params": {}
            }))
            await ws.recv()

            print("\n✓ Melody with bass line complete!")
            print(f"  Total notes added: {total_notes}")
            print("  Structure:")
            print("    - Melody: Upper staff (starting at MIDI 60)")
            print("    - Bass: Lower staff (starting at MIDI 48)")
            print("    - Bass supports harmonic structure")
            print("  Play in MuseScore: Press spacebar\n")

    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(compose_melody_with_bass())

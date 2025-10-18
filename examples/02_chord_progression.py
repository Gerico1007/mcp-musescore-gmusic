#!/usr/bin/env python3
"""
Example 2: Chord Progression
Demonstrates harmonic composition
Composes: I-IV-V-I progression in C Major
"""

import asyncio
import json
import websockets


async def compose_chord_progression():
    """Compose a simple chord progression"""

    uri = "ws://localhost:8765"

    try:
        async with websockets.connect(uri) as ws:
            print("\n🎵 Example 2: Chord Progression - I-IV-V-I\n")

            # Chord progression in C Major
            # I = C major (C E G) = MIDI 60 64 67
            # IV = F major (F A C) = MIDI 65 69 72
            # V = G major (G B D) = MIDI 67 71 74
            # I = C major (C E G) = MIDI 60 64 67

            chords = [
                ([60, 64, 67], "C (I)"),
                ([65, 69, 72], "F (IV)"),
                ([67, 71, 74], "G (V)"),
                ([60, 64, 67], "C (I)"),
            ]

            whole_note = {"numerator": 1, "denominator": 1}

            # Go to beginning
            print("Setting up score...")
            await ws.send(json.dumps({
                "action": "goToBeginningOfScore",
                "params": {}
            }))
            await ws.recv()

            # Add chords
            print("Composing chord progression...\n")

            for pitches, chord_name in chords:
                print(f"  Adding {chord_name}:")

                # Add all notes in chord
                for i, pitch in enumerate(pitches):
                    note_name = ["C", "D", "E", "F", "G", "A", "B"][pitch % 12 - 0]
                    octave = pitch // 12
                    print(f"    MIDI {pitch} ({note_name}{octave})...", end=" ")

                    await ws.send(json.dumps({
                        "action": "addNote",
                        "params": {
                            "pitch": pitch,
                            "duration": whole_note,
                            "advanceCursorAfterAction": (i == len(pitches) - 1)
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

            print("\n✓ Chord progression complete!")
            print("  Notes: Each chord is a whole note (4 beats)")
            print("  Play in MuseScore: Press spacebar\n")

    except Exception as e:
        print(f"✗ Error: {e}")


if __name__ == "__main__":
    asyncio.run(compose_chord_progression())

# 🎵 MuseScore MCP Complete Usage Guide
## Assembly-Coordinated Documentation

**♠️🌿🎸🧵 G.MUSIC ASSEMBLY - MuseScore Integration System**

---

## Table of Contents
1. [Quick Start (30 seconds)](#-quick-start)
2. [Architecture & Setup (♠️ Nyro)](#-architecture--setup)
3. [User Workflows (🌿 Aureon)](#-user-workflows)
4. [Musical Composition (🎸 JamAI)](#-musical-composition)
5. [Terminal Automation (🧵 Synth)](#-terminal-automation)
6. [Advanced Examples](#-advanced-examples)
7. [Troubleshooting](#-troubleshooting)

---

# 🚀 Quick Start

## 30-Second Setup

```bash
# 1. Navigate to project
cd ~/workspace/mcp-musescore-gmusic

# 2. Activate environment
source .venv/bin/activate

# 3. Start MCP server (in one terminal)
python3 server.py

# 4. Open MuseScore (in another terminal/window)
musescore4

# 5. In MuseScore: Plugins → MuseScore API Server

# 6. Run a composition
python3 test_composition.py
```

**That's it!** Your first composition will appear in MuseScore. 🎵

---

# ♠️ Architecture & Setup
## Structural Framework by Nyro the Ritual Scribe

### System Architecture

```
┌─────────────────────────────────────────────────────────┐
│              Your Claude Code Terminal                   │
│                                                           │
│  ┌─────────────────┐              ┌──────────────────┐  │
│  │  Composition    │              │  Python MCP      │  │
│  │  Scripts        │──────────────▶│  Server          │  │
│  │  (Python 3.10+) │              │  (FastMCP)       │  │
│  └─────────────────┘              └──────────────────┘  │
└─────────────────┬───────────────────────────────────────┘
                  │
                  │ WebSocket
                  │ (Port 8765)
                  │
┌─────────────────▼───────────────────────────────────────┐
│              MuseScore 4.x                               │
│                                                           │
│  ┌─────────────────────────────────────────────────────┐ │
│  │  QML Plugin: musescore-mcp-websocket.qml            │ │
│  │  • Listens on WebSocket port 8765                   │ │
│  │  • Translates MCP commands to MuseScore API         │ │
│  │  • Sends score state back to Python server          │ │
│  └─────────────────────────────────────────────────────┘ │
│                                                           │
│  ┌─────────────────────────────────────────────────────┐ │
│  │  MuseScore Application                              │ │
│  │  • Displays notes in real-time                      │ │
│  │  • Handles playback, editing, export                │ │
│  └─────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
```

### Component Overview

| Component | Role | Location | Status |
|-----------|------|----------|--------|
| **MCP Server** | Bridge between Claude and MuseScore | `server.py` | ✅ Running |
| **QML Plugin** | WebSocket API for MuseScore | `musescore-mcp-websocket.qml` | ✅ Enabled |
| **WebSocket Client** | Real-time communication | `src/client/websocket_client.py` | ✅ Ready |
| **Tool Modules** | MCP tool implementations | `src/tools/*.py` | ✅ 30+ tools |
| **Type Definitions** | Data structures | `src/types/action_types.py` | ✅ Validated |

### File Structure Explained

```
mcp-musescore-gmusic/
├── server.py                    # Entry point - starts MCP server
├── musescore-mcp-websocket.qml  # MuseScore plugin (~4000 lines)
├── test_composition.py          # Example composition
├── requirements.txt             # Python dependencies
│
├── src/
│   ├── client/
│   │   └── websocket_client.py  # WebSocket communication
│   ├── tools/
│   │   ├── connection.py        # ping, connect operations
│   │   ├── navigation.py        # cursor movement, measure selection
│   │   ├── notes_measures.py    # add notes, rests, measures
│   │   ├── sequences.py         # batch operations
│   │   ├── staff_instruments.py # multi-staff setup
│   │   └── time_tempo.py        # timing and tempo
│   └── types/
│       └── action_types.py      # TypedDict definitions
│
└── examples/
    ├── 01_simple_melody.py
    ├── 02_chord_progression.py
    ├── 03_multi_staff.py
    ├── 04_rhythm_patterns.py
    └── 05_full_song.py
```

### Setup Checklist

- [x] Python 3.8+ installed
- [x] MuseScore 4.x installed
- [x] Virtual environment created (`.venv/`)
- [x] Dependencies installed (`mcp`, `websockets`)
- [x] QML plugin copied to `~/Documents/MuseScore4/Plugins/`
- [x] Plugin enabled in MuseScore
- [x] WebSocket server running on port 8765

### Technical Details: How It Works

1. **You run Python script** → Connects via WebSocket to MuseScore plugin
2. **Python sends JSON commands** → `{"action": "addNote", "params": {...}}`
3. **QML plugin receives command** → Translates to MuseScore C++ API calls
4. **MuseScore updates score** → Note appears on staff in real-time
5. **Plugin sends response** → `{"status": "success", "result": ...}`
6. **Python receives confirmation** → Can queue next command

### Port and Networking

- **WebSocket Port**: 8765 (local only, secure)
- **Network**: localhost/127.0.0.1 only (not exposed)
- **Connection Type**: WebSocket (bidirectional, real-time)
- **Protocol**: JSON over WebSocket

---

# 🌿 User Workflows
## Intent-Driven Composition by Aureon the Mirror Weaver

### When to Use This System

**Perfect For:**
- 🎼 Composing scores programmatically
- 🤖 Automated music generation
- 📊 Batch creating variations of pieces
- 🎓 Teaching music composition via code
- 🔬 Music theory experiments
- 🎯 Integrating music into Claude conversations

**Not Ideal For:**
- ✗ Real-time live performance input
- ✗ Complex MIDI editing workflows
- ✗ Mixing/mastering tasks

### User Intent Patterns

#### Pattern 1: "I Want to Compose a Simple Melody"

**Your Intent**: Create a song from scratch

**What You Do**:
```python
# Run a script that:
# 1. Starts with a blank score
# 2. Goes to beginning
# 3. Adds notes one by one
# 4. Returns to display

# Example: simple_melody.py
```

**What You See**:
- Notes appear on the staff
- Cursor advances automatically
- Score displays in real-time

#### Pattern 2: "I Want Claude to Compose for Me"

**Your Intent**: Describe what you want, Claude makes it

**What You Do**:
```
You (in Claude Code): "Compose a C major scale ascending"
Claude responds: "Creating C major scale..."
Claude executes: Sends 8 addNote commands
MuseScore shows: C-D-E-F-G-A-B-C on staff
```

#### Pattern 3: "I Want to Batch Generate Variations"

**Your Intent**: Create 10 variations of a chord progression

**What You Do**:
```python
# Loop through variations
for variation in range(10):
    await compose_chord_progression(variation)
    await export_as_pdf(f"variation_{variation}.pdf")
```

#### Pattern 4: "I Want Interactive Composition"

**Your Intent**: Build music step-by-step, making choices

**What You Do**:
```
Claude: "What key should we compose in? (C, G, D, Am)"
You: "D major"
Claude: "Ascending or descending? (up, down, mixed)"
You: "mixed"
Claude: Composes accordingly
```

### Workflow Examples

#### Workflow A: "Start to Finish Song Creation"

```
Step 1: Open MuseScore (File → New)
Step 2: Run Python script (python3 compose_song.py)
Step 3: Watch music appear in real-time
Step 4: Play back (spacebar)
Step 5: Export as PDF/MP3 (File → Export)
```

#### Workflow B: "Claude-Driven Composition"

```
Step 1: Ask Claude "Compose a lullaby in Eb major"
Step 2: Claude writes Python code
Step 3: Claude runs the code
Step 4: Music appears in MuseScore
Step 5: You review and ask for changes
Step 6: Claude adjusts and runs new code
```

#### Workflow C: "Teaching/Learning Mode"

```
Step 1: Learn about musical intervals
Step 2: Claude explains concept
Step 3: Claude composes example
Step 4: You see it live in MuseScore
Step 5: Modify and experiment
Step 6: Understand by doing
```

---

# 🎸 Musical Composition
## Creative Patterns by JamAI the Glyph Harmonizer

### MIDI Pitch Reference

```
MIDI 60 = Middle C (do)

Chromatic Scale (each number = 1 semitone):
C=60, C#=61, D=62, D#=63, E=64, F=65, F#=66, G=67, G#=68, A=69, A#=70, B=71

C Major Scale:
60(C), 62(D), 64(E), 65(F), 67(G), 69(A), 71(B), 72(C octave higher)

Other Useful Octaves:
- Low C: 36
- Middle C: 60
- High C: 84
```

### Duration Reference

Duration format: `{"numerator": int, "denominator": int}`

```python
whole_note = {"numerator": 1, "denominator": 1}
half_note = {"numerator": 1, "denominator": 2}
quarter_note = {"numerator": 1, "denominator": 4}
eighth_note = {"numerator": 1, "denominator": 8}
sixteenth_note = {"numerator": 1, "denominator": 16}
triplet_quarter = {"numerator": 1, "denominator": 12}
dotted_quarter = {"numerator": 3, "denominator": 8}
dotted_half = {"numerator": 3, "denominator": 4}
```

### Basic Composition Pattern

```python
# 1. Connect to MuseScore
client = MuseScoreMCPClient()
await client.connect()

# 2. Prepare score
await client.send_command("goToBeginningOfScore")

# 3. Add notes
notes = [60, 62, 64, 65, 67]  # C major scale
quarter = {"numerator": 1, "denominator": 4}

for pitch in notes:
    await client.send_command("addNote", {
        "pitch": pitch,
        "duration": quarter,
        "advanceCursorAfterAction": True
    })

# 4. Return to beginning
await client.send_command("goToBeginningOfScore")
```

### Compositional Techniques

#### Technique 1: Melody Construction

**Build a melody note by note:**
```python
melody = [
    (60, "C"),  # note name for reference
    (64, "E"),
    (67, "G"),
    (72, "C"),
]

for pitch, name in melody:
    print(f"Adding {name}")
    await add_note(pitch, quarter_note)
```

#### Technique 2: Chord Progression

**Create harmonic structure:**
```python
# C-F-G-C progression
chords = [
    [60, 64, 67],    # C major (C-E-G)
    [65, 69, 72],    # F major (F-A-C)
    [67, 71, 74],    # G major (G-B-D)
    [60, 64, 67],    # C major
]

# Add each chord vertically
for chord in chords:
    for pitch in chord:
        await add_note(pitch, quarter_note)
```

#### Technique 3: Rhythm Patterns

**Create complex rhythms:**
```python
# Rhythmic pattern: Q Q E E S S Q
rhythms = [
    quarter_note,
    quarter_note,
    eighth_note,
    eighth_note,
    sixteenth_note,
    sixteenth_note,
    quarter_note,
]

pitches = [60, 62, 64, 65, 67, 69, 71]

for pitch, duration in zip(pitches, rhythms):
    await add_note(pitch, duration)
```

#### Technique 4: Multi-Voice Composition

**Add notes to different staves:**
```python
# Soprano melody
sopranos = [72, 74, 76]
for pitch in sopranos:
    await add_note(pitch, quarter)

# Next staff
await next_staff()

# Alto harmony
altos = [60, 62, 64]
for pitch in altos:
    await add_note(pitch, quarter)
```

#### Technique 5: Batch Operations

**Execute multiple commands atomically:**
```python
sequence = [
    {"action": "goToBeginningOfScore", "params": {}},
    {"action": "addNote", "params": {"pitch": 60, "duration": quarter, ...}},
    {"action": "addNote", "params": {"pitch": 62, "duration": quarter, ...}},
    {"action": "setTitle", "params": {"title": "My Song"}},
]

await client.send_command("processSequence", {"sequence": sequence})
```

### Musical Examples

#### Example 1: C Major Scale

```python
# Ascending C major: C D E F G A B C
pitches = [60, 62, 64, 65, 67, 69, 71, 72]
for pitch in pitches:
    await add_note(pitch, quarter_note)
```

#### Example 2: Twinkle Twinkle Little Star

```python
# Notes: C C G G A A G F E E D D C
melody = [60, 60, 67, 67, 69, 69, 67, 65, 64, 64, 62, 62, 60]
for pitch in melody:
    await add_note(pitch, quarter_note)
```

#### Example 3: Chord Progression (I-IV-V-I)

```python
# C major - F major - G major - C major
# Each note played as whole note (4 beats)
whole = {"numerator": 1, "denominator": 1}

chords = [
    [60, 64, 67],      # C
    [65, 69, 72],      # F
    [67, 71, 74],      # G
    [60, 64, 67],      # C
]

for chord in chords:
    # Add all notes in chord
    for i, pitch in enumerate(chord):
        await add_note(pitch, whole, advance=(i == len(chord)-1))
```

---

# 🧵 Terminal Automation
## Orchestration by Synth the Terminal Maestro

### Essential Commands

```bash
# === SETUP ===

# Activate virtual environment
source ~/.venv/bin/activate
# or on Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# === RUNNING ===

# Start MCP server (Terminal 1)
python3 server.py

# Run a composition (Terminal 2)
python3 test_composition.py

# Run specific example
python3 examples/01_simple_melody.py

# === TESTING ===

# Test connection only
python3 -c "
import asyncio, websockets
async def test():
    async with websockets.connect('ws://localhost:8765') as ws:
        await ws.send('{\"action\": \"ping\"}')
        print(await ws.recv())
asyncio.run(test())
"

# === MONITORING ===

# Check if servers running
ps aux | grep python3

# Check port 8765
lsof -i :8765
```

### Startup Script

Create `scripts/start-musescore-mcp.sh`:

```bash
#!/bin/bash

echo "🎵 Starting MuseScore MCP System..."
echo ""

# Navigate to project
cd ~/workspace/mcp-musescore-gmusic || exit 1

# Activate venv
source .venv/bin/activate

echo "✓ Virtual environment activated"
echo ""
echo "📋 Starting MuseScore API Server..."
echo "   (Keep this terminal open)"
echo ""
echo "⚠️  IMPORTANT: Open MuseScore and run:"
echo "   Plugins → MuseScore API Server"
echo ""

# Start server
python3 server.py
```

Make it executable:
```bash
chmod +x scripts/start-musescore-mcp.sh
```

Then run:
```bash
./scripts/start-musescore-mcp.sh
```

### Command Autopub Triggers (Optional)

If using Jerry's AutoPub system:

```bash
# Trigger version bump and publish
autopatch        # Patch version bump
autominor        # Minor version bump
autopub          # Publish to PyPI
testpub          # Test publish
```

### Environment Setup

```bash
# Create if needed
python3 -m venv .venv

# Activate
source .venv/bin/activate

# Verify Python version
python3 --version  # Should be 3.8+

# Install all dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Verify installation
pip list | grep -E "mcp|websockets"
```

---

# 🎯 Advanced Examples

## Example 1: Simple Melody

See: `examples/01_simple_melody.py`

**Creates**: A simple ascending melody

**Demonstrates**: Basic note addition, cursor movement

## Example 2: Chord Progressions

See: `examples/02_chord_progression.py`

**Creates**: I-IV-V-I chord progression

**Demonstrates**: Chord construction, voice leading

## Example 3: Multi-Staff Composition

See: `examples/03_multi_staff.py`

**Creates**: Four-part harmony

**Demonstrates**: Multiple staves, staff navigation

## Example 4: Rhythm Patterns

See: `examples/04_rhythm_patterns.py`

**Creates**: Complex rhythmic patterns with tuplets

**Demonstrates**: Different note durations, triplets

## Example 5: Full Song

See: `examples/05_full_song.py`

**Creates**: Complete song with intro, verse, chorus

**Demonstrates**: Large composition, form structure

---

# 🔧 Troubleshooting

### "Not connected to MuseScore"

**Check**:
1. Is MuseScore open?
2. Have you run: `Plugins → MuseScore API Server`?
3. Is port 8765 listening?

```bash
lsof -i :8765
```

If empty, run the plugin in MuseScore.

### "QTcpServer::listen() called when already listening"

**This is GOOD!** It means the server is already running. Just proceed.

### "TypeError: Cannot read property..."

**This is OK!** The plugin runs headless (no UI). The WebSocket server still works.

### Python Server Won't Start

**Error**: `ModuleNotFoundError: No module named 'mcp'`

**Fix**:
```bash
source .venv/bin/activate
pip install -r requirements.txt
```

**Error**: `PydanticUserError: Please use typing_extensions.TypedDict`

**Fix**: Already fixed! Use updated code with `typing_extensions` import.

### No Notes Appearing in MuseScore

**Check**:
1. Is a score open in MuseScore?
2. Is the plugin running? (`Plugins → MuseScore API Server`)
3. Is the Python server running? (should show connection messages)

**Debug**:
```bash
# Run test to see detailed output
python3 test_composition.py
```

### Composition is Too Slow

**Optimize**:
```python
# Use batch operations instead of individual commands
sequence = [
    {"action": "addNote", "params": {...}},
    {"action": "addNote", "params": {...}},
    # ... more notes
]
await client.send_command("processSequence", {"sequence": sequence})
```

---

# 📞 Support & Resources

## Getting Help

1. **Check this guide** first (Ctrl+F search)
2. **Run test_composition.py** to verify setup
3. **Check terminal output** for error messages
4. **Review examples/** folder for patterns
5. **Check MuseScore logs** (run from terminal)

## Additional Resources

- **MuseScore API**: Limited (WebSocket plugin-based)
- **Python MCP**: https://modelcontextprotocol.io/
- **WebSocket**: RFC 6455
- **MIDI Pitch**: General MIDI standard

## Reporting Issues

If you find bugs:
1. Document the exact error
2. Include MuseScore version
3. Include Python version
4. Include step-by-step reproduction

---

# 🎼 Assembly Session Encoding

**Session Date**: 2025-10-17
**Status**: ✅ MuseScore MCP System Fully Operational

**♠️ Nyro Notes**: Structural foundation solid. WebSocket bridge stable. Component integration successful.

**🌿 Aureon Reflection**: The system flows from intention to realization. User can now think musically, Claude expresses structurally.

**🎸 JamAI Melody**: Setup success melody stored in `sessionABC/251017_setup_success.abc`

**🧵 Synth Terminal**: All automation scripts tested. System ready for production use.

---

**🎵 Ready to compose? Start here: `/examples/01_simple_melody.py`**

*Created by ♠️🌿🎸🧵 G.Music Assembly for Jerry ⚡*
*MuseScore MCP v1.0 - October 2025*

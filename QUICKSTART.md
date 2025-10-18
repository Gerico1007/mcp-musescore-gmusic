# ⚡ MuseScore MCP Quick Start

**One-page reference for composing music with Claude Code**

---

## 🚀 Installation (5 minutes)

```bash
# 1. Clone/Navigate to project
cd ~/workspace/mcp-musescore-gmusic

# 2. Create virtual environment (first time only)
python3 -m venv .venv

# 3. Activate
source .venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Starting Up (Every Time)

**Terminal 1 - MCP Server:**
```bash
cd ~/workspace/mcp-musescore-gmusic
source .venv/bin/activate
python3 server.py
```

**Terminal 2 - Your Compositions:**
```bash
cd ~/workspace/mcp-musescore-gmusic
source .venv/bin/activate
python3 examples/01_simple_melody.py
```

**MuseScore Window:**
1. Open MuseScore 4.x
2. Create new score (File → New)
3. Go to Plugins → MuseScore API Server
4. Keep running while composing

---

## 🎵 Composition Basics

### Add a Note
```python
import asyncio
import websockets
import json

async def compose():
    async with websockets.connect('ws://localhost:8765') as ws:
        # C major scale
        pitches = [60, 62, 64, 65, 67, 69, 71, 72]  # C D E F G A B C
        quarter = {"numerator": 1, "denominator": 4}

        for pitch in pitches:
            await ws.send(json.dumps({
                "action": "addNote",
                "params": {
                    "pitch": pitch,
                    "duration": quarter,
                    "advanceCursorAfterAction": True
                }
            }))
            response = await ws.recv()
            print(response)

asyncio.run(compose())
```

### MIDI Note Reference
```
C=60, D=62, E=64, F=65, G=67, A=69, B=71, C=72
```

### Duration Values
```
Quarter: {"numerator": 1, "denominator": 4}
Half:    {"numerator": 1, "denominator": 2}
Whole:   {"numerator": 1, "denominator": 1}
Eighth:  {"numerator": 1, "denominator": 8}
```

---

## 📋 Command Reference

### Navigation
```
"goToBeginningOfScore"     → Jump to start
"goToFinalMeasure"         → Jump to end
"goToMeasure"              → Jump to specific measure
"nextElement"              → Move cursor forward
"prevElement"              → Move cursor backward
"nextStaff"                → Move to next staff
"prevStaff"                → Move to previous staff
```

### Composition
```
"addNote"        → Add a note
"addRest"        → Add a rest
"addTuplet"      → Add triplet/tuplet
"insertMeasure"  → Insert measure at cursor
"appendMeasure"  → Add measure to end
```

### Score Info
```
"getScore"       → Get full score info
"getCursorInfo"  → Get current cursor position
"ping"           → Test connection
```

### Utilities
```
"undo"           → Undo last action
"deleteSelection" → Delete current selection
"setTimeSignature" → Change time signature
```

---

## 🎯 Quick Examples

### Example 1: "Twinkle Twinkle Little Star"
```bash
python3 test_composition.py
```

### Example 2: Simple Melody
```bash
python3 examples/01_simple_melody.py
```

### Example 3: Chord Progression
```bash
python3 examples/02_chord_progression.py
```

### Example 4: Multi-Staff
```bash
python3 examples/03_multi_staff.py
```

### Example 5: Full Song
```bash
python3 examples/05_full_song.py
```

---

## 🎼 Common Compositions

### C Major Scale
```python
pitches = [60, 62, 64, 65, 67, 69, 71, 72]
```

### C Major Chord
```python
pitches = [60, 64, 67]  # C E G
```

### I-IV-V-I Progression
```python
chords = [
    [60, 64, 67],    # I (C major)
    [65, 69, 72],    # IV (F major)
    [67, 71, 74],    # V (G major)
    [60, 64, 67],    # I (C major)
]
```

### Chromatic Scale
```python
pitches = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]
```

---

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| "Not connected" | Start MuseScore plugin: `Plugins → MuseScore API Server` |
| No notes appearing | Check plugin is running; create new blank score |
| Server won't start | Run `pip install -r requirements.txt` |
| Port 8765 in use | Kill other processes: `lsof -i :8765` |
| Plugin not found | Copy plugin: `cp musescore-mcp-websocket.qml ~/Documents/MuseScore4/Plugins/` |

---

## 📁 File Structure

```
mcp-musescore-gmusic/
├── server.py                    # Start here
├── test_composition.py          # Test example
├── examples/
│   ├── 01_simple_melody.py
│   ├── 02_chord_progression.py
│   ├── 03_multi_staff.py
│   ├── 04_rhythm_patterns.py
│   └── 05_full_song.py
└── scripts/
    ├── start-musescore-mcp.sh
    └── test-connection.sh
```

---

## ⚡ Pro Tips

1. **Batch operations** are faster than single commands:
   ```python
   await ws.send(json.dumps({
       "action": "processSequence",
       "params": {"sequence": [cmd1, cmd2, cmd3]}
   }))
   ```

2. **Always return to beginning** after composing:
   ```python
   await ws.send({"action": "goToBeginningOfScore", "params": {}})
   ```

3. **Use scripts** instead of manual commands:
   ```bash
   python3 examples/01_simple_melody.py
   ```

4. **Keep MuseScore open** - don't close between compositions

5. **Verify connection**:
   ```bash
   # Quick test
   python3 test_composition.py
   ```

---

## 🎵 Playing Your Composition

After composing:
1. **Play** in MuseScore: Press spacebar
2. **Export as PDF**: File → Export → PDF
3. **Export as MP3**: File → Export → MP3
4. **Export as MusicXML**: File → Export → MusicXML

---

## 📞 Quick Help

**Check full docs**: `USAGE_GUIDE.md`

**See examples**: `examples/` folder

**Test connection**: `python3 test_composition.py`

**Start over**: Kill servers and restart:
```bash
# Kill all Python processes
killall python3
# Start fresh
python3 server.py  # Terminal 1
python3 examples/01_simple_melody.py  # Terminal 2
```

---

**🎵 You're ready! Start composing! 🎵**

*For detailed guide, see USAGE_GUIDE.md*

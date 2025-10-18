# 🎵 Using MuseScore MCP Directly with Claude Code

Now you can ask me to compose music directly! No more Python scripts needed.

---

## 🚀 Quick Start

### Step 1: Make Sure Servers are Running

**Terminal 1 - Start Python MCP Server:**
```bash
cd ~/workspace/mcp-musescore-gmusic
source .venv/bin/activate
python3 server.py
```

**MuseScore Window:**
```
Plugins → MuseScore API Server
```

### Step 2: Launch Claude Code with MCP

**Terminal 2 - Start Claude Code with MCP:**
```bash
./scripts/claude-compose.sh
```

Or manually:
```bash
claude-code --mcp musescore
```

### Step 3: Ask Me to Compose!

Just ask in Claude Code:

```
"Compose a C Major scale"
"Add a bass line to support the melody"
"Create a I-IV-V-I chord progression"
"Write 'Happy Birthday' in G Major"
```

I'll use the MCP tools directly to compose in MuseScore! 🎵

---

## 📋 MCP Tools Available

### Navigation
- `go_to_beginning_of_score()` - Jump to start
- `go_to_final_measure()` - Jump to end
- `go_to_measure(measure_number)` - Jump to specific measure
- `next_element()` - Move cursor forward
- `prev_element()` - Move cursor backward
- `next_staff()` - Move to next staff
- `prev_staff()` - Move to previous staff

### Composition
- `add_note(pitch, duration, advance_cursor_after_action)` - Add a note
- `add_rest(duration, advance_cursor_after_action)` - Add a rest
- `add_tuplet(duration, ratio, advance_cursor_after_action)` - Add triplets

### Score Management
- `insert_measure()` - Insert measure at cursor
- `append_measure(count)` - Add measures to end
- `delete_selection(measure)` - Delete current selection
- `getScore()` - Get full score information

### Utilities
- `ping_musescore()` - Test connection
- `undo()` - Undo last action
- `get_cursor_info()` - Get cursor position

---

## 💡 Example Requests

### "Compose a C Major scale"
I'll call:
```
add_note(60, quarter_note)  # C
add_note(62, quarter_note)  # D
add_note(64, quarter_note)  # E
add_note(65, quarter_note)  # F
add_note(67, quarter_note)  # G
add_note(69, quarter_note)  # A
add_note(71, quarter_note)  # B
add_note(72, quarter_note)  # C
go_to_beginning_of_score()
```

### "Add a bass line"
I'll call:
```
next_staff()
add_note(48, half_note)    # C (low)
add_note(53, half_note)    # F
add_note(55, half_note)    # G
add_note(48, half_note)    # C
go_to_beginning_of_score()
```

### "Create a I-IV-V-I progression"
I'll call:
```
# Add chords to different staves
add_note(60, whole_note)   # C chord
add_note(65, whole_note)   # F chord
add_note(67, whole_note)   # G chord
add_note(60, whole_note)   # C chord
```

---

## 🎼 MIDI Pitch Reference

```
C=60, D=62, E=64, F=65, G=67, A=69, B=71

Octaves:
- Low: 24-47
- Middle: 48-71  ← Most common for melody/bass
- High: 72-95

Examples:
- Middle C: 60
- Low C: 48
- High C: 84
```

---

## ⏱️ Duration Values

```python
whole_note = {"numerator": 1, "denominator": 1}
half_note = {"numerator": 1, "denominator": 2}
quarter_note = {"numerator": 1, "denominator": 4}
eighth_note = {"numerator": 1, "denominator": 8}
sixteenth_note = {"numerator": 1, "denominator": 16}
dotted_quarter = {"numerator": 3, "denominator": 8}
triplet_quarter = {"numerator": 1, "denominator": 12}
```

---

## 🎯 What You Can Ask Me

### Composition Tasks
- ✓ "Compose a melody"
- ✓ "Add a bass line"
- ✓ "Create chord progression"
- ✓ "Write this song"
- ✓ "Add harmony parts"
- ✓ "Create rhythm patterns"

### Editing Tasks
- ✓ "Go to measure 8"
- ✓ "Insert 4 measures"
- ✓ "Delete this section"
- ✓ "Undo the last note"

### Analysis Tasks
- ✓ "What's the current score state?"
- ✓ "How many measures are there?"
- ✓ "Test the connection"

---

## 📊 Configuration

**Config Location**: `~/.config/claude-code/mcp_servers.json`

```json
{
  "mcpServers": {
    "musescore": {
      "command": "python3",
      "args": [
        "/home/gmusic/workspace/mcp-musescore-gmusic/server.py"
      ]
    }
  }
}
```

**Launcher**: `./scripts/claude-compose.sh`

---

## 🔧 Troubleshooting

### "MCP server not found"
- Make sure `python3 server.py` is running
- Make sure MuseScore plugin is enabled

### "Connection refused"
- Check port 8765 is listening: `lsof -i :8765`
- Run MuseScore plugin: `Plugins → MuseScore API Server`

### "Claude Code doesn't recognize MCP"
- Check config file exists: `~/.config/claude-code/mcp_servers.json`
- Verify JSON is valid (no syntax errors)
- Restart Claude Code

---

## 🚀 Direct Usage Examples

### Example 1: Simple Request
```
User: "Compose a G major arpeggio"

Claude:
I'll compose a G major arpeggio (G-B-D) for you.
```
I call: add_note(67), add_note(71), add_note(74)

### Example 2: Complex Request
```
User: "Create a song with verse and chorus"

Claude:
I'll create a song structure with:
- Verse: C-D-E-F-G progression
- Chorus: G-G-A-B-C progression
```
I call multiple add_note() commands

### Example 3: Interactive
```
User: "What key should we compose in?"

Claude:
What key would you prefer? (C, G, D, Am, Em, etc.)

User: "D Major"

Claude:
Great! Composing in D Major...
```
I call composition tools based on your input

---

## 💬 How to Ask Effectively

**Good Requests:**
- "Compose a C Major scale ascending"
- "Add a bass line in C"
- "Create a I-IV-V-I chord progression in G Major"
- "Write this melody: C D E F G"

**Less Clear:**
- "Make some music"
- "Compose something nice"
- "Add stuff to the score"

**Pro Tips:**
- Mention the key
- Specify the structure (verse/chorus, intro/outro)
- Give MIDI notes or note names
- Describe the rhythm pattern
- Request specific instrumentation (melody/bass/harmony)

---

## 📞 Quick Commands

```bash
# Start MCP server
python3 server.py

# Start Claude Code with MCP
./scripts/claude-compose.sh

# Test connection
./scripts/test-connection.sh

# Run example
python3 examples/01_simple_melody.py
```

---

## ✨ You're Ready!

Now you can compose directly with Claude Code! No Python scripts needed. Just ask me what you want to create, and I'll use the MCP tools to compose it in MuseScore in real-time.

**♠️🌿🎸🧵 Direct MCP Composition Ready!**

Start with: "Compose a melody of your choice in C Major"

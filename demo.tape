# Demo tape for ctxguard — recorded by charmbracelet/vhs
# https://github.com/charmbracelet/vhs
#
# Renders to demo.gif via `vhs demo.tape`.
# Reads /tmp/demo-session.jsonl which is pre-populated with 6 fake assistant turns.

Output demo.gif

Set Shell bash
Set FontSize 14
Set Width 1200
Set Height 720
Set Padding 20
Set Theme "Catppuccin Mocha"

# 1. Hook
Type "ctxguard --version"
Sleep 500ms
Enter
Sleep 1s

# 2. Profile across 7 days, by day
Type "ctxguard profile --days 7 --by day"
Sleep 500ms
Enter
Sleep 4s

# 3. Show the headline number: 2.1B context tokens
Sleep 2s

# 4. Drill into a single session
Type "ctxguard parse /tmp/demo-session.jsonl"
Sleep 500ms
Enter
Sleep 3s

# 5. Live budget enforcement — wrap a sleep with budget=5000
Type "ctxguard run --budget 5000 --on-full warn --session /tmp/demo-session.jsonl -- sleep 30 &"
Sleep 500ms
Enter
Sleep 1s

# 6. Background process prints "watching"
Type "# in another terminal: append a few turns to /tmp/demo-session.jsonl"
Sleep 1s
Enter
Sleep 2s

# 7. Show budget hit warning
Sleep 3s

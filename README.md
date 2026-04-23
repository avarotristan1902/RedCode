# 🔴 RedCode Programming Language

RedCode is a lightweight, custom programming language interpreter built with Python on **Pydroid 3**. It is designed to be simple, colorful, and powerful enough to run logic and loops directly on an Android device.

## 🚀 Latest Update: v2.5 (The Logic & Loop Update)
We have officially moved past basic commands! RedCode now supports:
- **Variables & Memory:** Store data using `SET`.
- **Advanced Math:** Use `CALC` for complex expressions like `(5 + 2) * 10`.
- **Logic & Decisions:** Use `IF` statements to make your code "smart."
- **Automation:** `WHILE` loops and `REPEAT` for running code multiple times.
- **External Scripts:** Use `RUN` to execute `.red` files saved on your device.

---

## 🛠️ Commands Reference


| Command | Usage | Description |
| :--- | :--- | :--- |
| **SET** | `SET x 10` | Stores a value in a variable. |
| **PRINT** | `PRINT Hello x` | Displays text or variable values. |
| **CALC** | `CALC result x + 5` | Performs math and saves to a variable. |
| **RANDOM** | `RANDOM d6 1 6` | Generates a random number. |
| **IF** | `IF x > 5 PRINT Win` | Runs a command if a condition is true. |
| **WHILE** | `WHILE x < 5` | Starts a loop (end with `ENDWHILE`). |
| **COLOR** | `COLOR RED` | Changes the terminal text color. |
| **RUN** | `RUN script.red` | Runs a saved RedCode file. |
| **SLEEP** | `SLEEP 1.5` | Pauses execution for X seconds. |

---

## 🎮 Example Script
Create a file named `game.red` and run it:
```red
# RedCode Counting Game
SET x 1
COLOR GREEN
PRINT Starting Count...

WHILE x < 6
  PRINT Number: x
  CALC x x + 1
  SLEEP 0.5
ENDWHILE

COLOR RESET
PRINT Done!
```

## 📲 How to Install on Android
1. Download [Pydroid 3](https://google.com) from the Play Store.
2. Copy the `redcode.py` code from this repository.
3. Paste it into Pydroid 3 and press **Play**.
4. Type your commands into the `RedCode >` prompt!

## 🗺️ Roadmap
- [x] Variables and Math
- [x] Loops and Logic
- [ ] **Functions / Subroutines** (Next Up!)
- [ ] User Input for Games
- [ ] 

name: Build EXE

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: windows-latest

    steps:
      - uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          pip install pyinstaller pyautogui pillow

      - name: Build EXE
        run: |
          pyinstaller --noconsole --onefile clicker_gui.py

      - name: Upload EXE
        uses: actions/upload-artifact@v2
        with:
          name: clicker-gui-exe
          path: dist/clicker_gui.exe

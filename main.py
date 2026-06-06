#!/usr/bin/env python3
"""
ASCII Art Generator — Advanced Edition
Create cool text art with different styles, gradients, and effects!
"""

import random
import sys
import time
import os

class AsciiArtGenerator:

    STYLES = {
        'banner': {
            'A': ['  ##  ', ' #  # ', '#    #', '######', '#    #', '#    #'],
            'B': ['##### ', '#    #', '##### ', '#    #', '#    #', '##### '],
            'C': [' #### ', '#    #', '#     ', '#     ', '#    #', ' #### '],
            'D': ['##### ', '#    #', '#    #', '#    #', '#    #', '##### '],
            'E': ['######', '#     ', '####  ', '#     ', '#     ', '######'],
            'F': ['######', '#     ', '####  ', '#     ', '#     ', '#     '],
            'G': [' #### ', '#     ', '#  ###', '#    #', '#    #', ' #### '],
            'H': ['#    #', '#    #', '######', '#    #', '#    #', '#    #'],
            'I': ['######', '  ##  ', '  ##  ', '  ##  ', '  ##  ', '######'],
            'J': ['    ##', '    # ', '    # ', '#   # ', '#   # ', ' ###  '],
            'K': ['#    #', '#   # ', '####  ', '#  #  ', '#   # ', '#    #'],
            'L': ['#     ', '#     ', '#     ', '#     ', '#     ', '######'],
            'M': ['#    #', '##  ##', '# ## #', '#    #', '#    #', '#    #'],
            'N': ['#    #', '##   #', '# #  #', '#  # #', '#   ##', '#    #'],
            'O': [' #### ', '#    #', '#    #', '#    #', '#    #', ' #### '],
            'P': ['##### ', '#    #', '##### ', '#     ', '#     ', '#     '],
            'Q': [' #### ', '#    #', '#    #', '#  # #', '#   # ', ' ### #'],
            'R': ['##### ', '#    #', '##### ', '#  #  ', '#   # ', '#    #'],
            'S': [' #### ', '#     ', ' #### ', '     #', '     #', ' #### '],
            'T': ['######', '  ##  ', '  ##  ', '  ##  ', '  ##  ', '  ##  '],
            'U': ['#    #', '#    #', '#    #', '#    #', '#    #', ' #### '],
            'V': ['#    #', '#    #', '#    #', '#    #', ' #  # ', '  ##  '],
            'W': ['#    #', '#    #', '#    #', '# ## #', '##  ##', '#    #'],
            'X': ['#    #', ' #  # ', '  ##  ', '  ##  ', ' #  # ', '#    #'],
            'Y': ['#    #', ' #  # ', '  ##  ', '  ##  ', '  ##  ', '  ##  '],
            'Z': ['######', '    # ', '   #  ', '  #   ', ' #    ', '######'],
            '0': [' #### ', '#   ##', '#  # #', '# #  #', '##   #', ' #### '],
            '1': ['  ##  ', ' ###  ', '  ##  ', '  ##  ', '  ##  ', '######'],
            '2': [' #### ', '#    #', '    # ', '  ##  ', ' #    ', '######'],
            '3': [' #### ', '#    #', '   ## ', '     #', '#    #', ' #### '],
            '!': ['  ##  ', '  ##  ', '  ##  ', '      ', '  ##  ', '  ##  '],
            '?': [' #### ', '#    #', '    # ', '   #  ', '      ', '   #  '],
            ' ': ['      ', '      ', '      ', '      ', '      ', '      '],
        }
    }

    COLORS = {
        'red':      '\033[91m',
        'green':    '\033[92m',
        'yellow':   '\033[93m',
        'blue':     '\033[94m',
        'magenta':  '\033[95m',
        'cyan':     '\033[96m',
        'white':    '\033[97m',
        'orange':   '\033[38;5;208m',
        'pink':     '\033[38;5;213m',
        'lime':     '\033[38;5;118m',
        'reset':    '\033[0m',
        'bold':     '\033[1m',
        'dim':      '\033[2m',
    }

    # Gradient sequences (color pairs for top-to-bottom gradient)
    GRADIENTS = {
        'sunset':   ['red', 'orange', 'yellow', 'orange', 'red', 'magenta'],
        'ocean':    ['blue', 'cyan', 'green', 'cyan', 'blue', 'blue'],
        'forest':   ['green', 'lime', 'yellow', 'lime', 'green', 'green'],
        'neon':     ['magenta', 'pink', 'cyan', 'lime', 'yellow', 'magenta'],
        'fire':     ['yellow', 'orange', 'red', 'red', 'orange', 'yellow'],
        'ice':      ['white', 'cyan', 'blue', 'cyan', 'white', 'white'],
    }

    BORDERS = {
        'stars':    ('★' + ' ★' * 29,        '★' + ' ★' * 29),
        'lines':    ('═' * 60,                '═' * 60),
        'fancy':    ('╔' + '═' * 58 + '╗',   '╚' + '═' * 58 + '╝'),
        'dots':     ('· ' * 30,               '· ' * 30),
        'hash':     ('# ' * 30,               '# ' * 30),
        'wave':     ('~≈' * 30,               '≈~' * 30),
        'minimal':  ('─' * 60,                '─' * 60),
    }

    FILL_CHARS = {
        'block':    '█',
        'shade':    '▓',
        'light':    '░',
        'hash':     '#',
        'at':       '@',
        'plus':     '+',
        'dot':      '·',
    }

    # ─── Core Render Helpers ──────────────────────────────────────────────────

    def _colorize(self, text, color):
        code = self.COLORS.get(color, '')
        reset = self.COLORS['reset']
        return f"{code}{text}{reset}" if code else text

    def _print_slow(self, text, delay=0.015):
        """Print text character-by-character for a typewriter effect."""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def _clear_line(self):
        sys.stdout.write('\r\033[K')
        sys.stdout.flush()

    # ─── Styles ───────────────────────────────────────────────────────────────

    def generate_banner(self, text, color='cyan', border='fancy', fill='#', gradient=None, animate=False):
        """
        Big-letter banner.
        New: gradient coloring per row, custom fill char, optional typewriter reveal.
        """
        text = text.upper()
        lines = [''] * 6

        for char in text:
            if char in self.STYLES['banner']:
                char_lines = self.STYLES['banner'][char]
                # Replace '#' placeholder with chosen fill character
                for i in range(6):
                    lines[i] += char_lines[i].replace('#', fill) + ' '
            else:
                for i in range(6):
                    lines[i] += '      '  # 6-space gap for unknown chars

        reset = self.COLORS['reset']
        top_border, bottom_border = self.BORDERS.get(border, ('─' * 60, '─' * 60))

        # Choose per-row colors
        if gradient and gradient in self.GRADIENTS:
            row_colors = self.GRADIENTS[gradient]
        else:
            row_colors = [color] * 6

        border_color = self.COLORS.get(color, '')

        print()
        print(f"{border_color}{top_border}{reset}")
        for i, line in enumerate(lines):
            row_color = self.COLORS.get(row_colors[i], '')
            rendered = f"{row_color}{line}{reset}"
            if animate:
                self._print_slow(rendered, delay=0.005)
            else:
                print(rendered)
        print(f"{border_color}{bottom_border}{reset}")
        print()

    def generate_wave(self, text, cycles=3):
        """
        Wavy text — now with color cycling across characters.
        """
        wave_chars = "~≈∿∼⋰⋱"
        colors = ['cyan', 'blue', 'magenta', 'green', 'yellow']
        print()
        for i in range(cycles):
            output = ""
            for j, char in enumerate(text):
                offset = (j + i) % len(wave_chars)
                col = self.COLORS.get(colors[(j + i) % len(colors)], '')
                reset = self.COLORS['reset']
                output += f"{col}{wave_chars[offset]} {char} {reset}"
            print(output)
        print()

    def generate_box(self, text, color='white', double_border=False):
        """
        Boxed text — now supports double-line Unicode box and color.
        """
        width = len(text) + 4
        if double_border:
            top    = '╔' + '═' * (width - 2) + '╗'
            middle = '║ ' + text + ' ║'
            bottom = '╚' + '═' * (width - 2) + '╝'
        else:
            top    = '┌' + '─' * (width - 2) + '┐'
            middle = '│ ' + text + ' │'
            bottom = '└' + '─' * (width - 2) + '┘'

        col   = self.COLORS.get(color, '')
        reset = self.COLORS['reset']
        print(f"\n{col}{top}\n{middle}\n{bottom}{reset}\n")

    def generate_shadow(self, text, color='white', shadow_char='▓'):
        """Shadow effect — now with configurable shadow character and color."""
        col   = self.COLORS.get(color, '')
        dim   = self.COLORS['dim']
        reset = self.COLORS['reset']
        shadow = ''.join([shadow_char if c != ' ' else ' ' for c in text])
        print(f"\n{col}{text}{reset}")
        print(f"{dim} {shadow}{reset}\n")

    def generate_rainbow(self, text, bold=False):
        """Rainbow text — bold option added."""
        colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
        bold_code = self.COLORS['bold'] if bold else ''
        output = ""
        for i, char in enumerate(text):
            color = colors[i % len(colors)]
            output += f"{bold_code}{self.COLORS[color]}{char}"
        output += self.COLORS['reset']
        print(f"\n{output}\n")

    def generate_stacked(self, text, fill='█', color='cyan'):
        """
        NEW: Render each letter stacked vertically as a filled block column.
        Gives a 'monument' feel — tall and monolithic.
        """
        col   = self.COLORS.get(color, '')
        reset = self.COLORS['reset']
        print()
        for char in text.upper():
            if char in self.STYLES['banner']:
                for row in self.STYLES['banner'][char]:
                    print(col + row.replace('#', fill) + reset)
            print()

    def generate_matrix(self, text, color='green', drops=5, duration=1.5):
        """
        NEW: Matrix-rain title card — streams of digits cascade, then text
        bursts through in the center.
        """
        cols   = 60
        col    = self.COLORS.get(color, '')
        reset  = self.COLORS['reset']
        start  = time.time()

        while time.time() - start < duration:
            line = ''
            for _ in range(cols):
                if random.random() < 0.1:
                    line += col + str(random.randint(0, 9)) + reset
                else:
                    line += ' '
            print(line)
            time.sleep(0.05)

        # Clear and show the text in a box
        self.generate_box(text, color=color, double_border=True)

    def generate_glitch(self, text, passes=4):
        """
        NEW: Glitch effect — prints corrupted versions of the text before
        resolving to the clean version.
        """
        glitch_chars = list('▓░▒█▀▄@#%&*!?/\\|')
        colors = ['red', 'magenta', 'cyan', 'white']

        for p in range(passes):
            glitched = ''
            for char in text:
                if random.random() < (0.6 - p * 0.12):   # fewer glitches each pass
                    glitched += random.choice(glitch_chars)
                else:
                    glitched += char
            col = self.COLORS.get(random.choice(colors), '')
            reset = self.COLORS['reset']
            print(f"\r{col}{glitched}{reset}", end='')
            time.sleep(0.12)

        # Final clean print
        print(f"\r{self.COLORS['white']}{text}{self.COLORS['reset']}\n")

    def generate_outline(self, text, color='yellow'):
        """
        NEW: Banner-style letters rendered as outlines only (hollow letters)
        using the corner/edge Unicode block chars.
        """
        text = text.upper()
        lines = [''] * 6
        col   = self.COLORS.get(color, '')
        reset = self.COLORS['reset']

        for char in text:
            if char in self.STYLES['banner']:
                char_lines = self.STYLES['banner'][char]
                for i in range(6):
                    # Replace inner '#' with '·' for a hollow look
                    row = char_lines[i]
                    if i in (1, 2, 3, 4) and len(row.strip()) > 2:
                        inner = list(row)
                        stripped = row.strip()
                        if len(stripped) > 2:
                            first = row.index(stripped[0])
                            last  = row.rindex(stripped[-1])
                            for k in range(first + 1, last):
                                if inner[k] == '#':
                                    inner[k] = '·'
                            row = ''.join(inner)
                    lines[i] += row + ' '

        print()
        for line in lines:
            print(col + line + reset)
        print()

    # ─── History & Export ─────────────────────────────────────────────────────

    def save_to_file(self, text, style, filename=None):
        """
        NEW: Save a plain-text (no ANSI) render to a .txt file.
        Uses the banner style for the exported version.
        """
        if filename is None:
            filename = f"ascii_{text[:10].replace(' ', '_')}.txt"

        text_upper = text.upper()
        lines = [''] * 6
        for char in text_upper:
            if char in self.STYLES['banner']:
                for i in range(6):
                    lines[i] += self.STYLES['banner'][char][i] + ' '

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"ASCII Art — Style: {style}\n")
            f.write("=" * 60 + "\n")
            for line in lines:
                f.write(line + "\n")
            f.write("=" * 60 + "\n")

        print(f"\n💾  Saved to {filename}\n")
        return filename


# ─── UI ───────────────────────────────────────────────────────────────────────

def display_menu():
    print("\n" + "╔" + "═" * 48 + "╗")
    print("║" + "    🎨  ASCII ART GENERATOR — ADVANCED    ".center(48) + "║")
    print("╠" + "═" * 48 + "╣")
    options = [
        ("1", "Banner Style       (big letters + gradient)"),
        ("2", "Wave Effect        (color-cycling)"),
        ("3", "Box Frame          (single or double border)"),
        ("4", "Shadow Effect      (custom shadow char)"),
        ("5", "Rainbow Colors     (bold option)"),
        ("6", "Stacked Monument   (letter-by-letter)"),
        ("7", "Matrix Rain        (animated title card)"),
        ("8", "Glitch Effect      (resolves to clean text)"),
        ("9", "Outline Letters    (hollow banner)"),
        ("S", "Save Last to File"),
        ("R", "Random Style"),
        ("Q", "Quit"),
    ]
    for key, label in options:
        print(f"║  [{key}] {label:<42}║")
    print("╚" + "═" * 48 + "╝")


def get_text(prompt="Enter your text: "):
    text = input(prompt).strip()
    if not text:
        print("⚠  Please enter some text.")
    return text


def main():
    g = AsciiArtGenerator()
    last_text  = ""
    last_style = "banner"

    print("\n✨  Welcome to ASCII Art Generator — Advanced Edition!  ✨")

    while True:
        display_menu()
        choice = input("\nChoose a style: ").strip().upper()

        if choice == 'Q':
            print("\n👋  Goodbye!\n")
            break

        if choice == 'S':
            if not last_text:
                print("⚠  Nothing to save yet — generate something first.")
                continue
            g.save_to_file(last_text, last_style)
            continue

        if choice == 'R':
            choice = str(random.randint(1, 9))
            print(f"   🎲  Random pick: option {choice}")

        text = get_text()
        if not text:
            continue

        last_text = text

        if choice == '1':
            colors  = [c for c in g.COLORS if c not in ('reset', 'bold', 'dim')]
            grads   = list(g.GRADIENTS.keys())
            fills   = list(g.FILL_CHARS.keys())
            borders = list(g.BORDERS.keys())
            print(f"  Colors:    {colors}")
            color   = input("  Color (default cyan):       ").strip() or 'cyan'
            print(f"  Gradients: {grads}  (overrides solid color)")
            grad    = input("  Gradient (blank for none):  ").strip() or None
            print(f"  Fill chars:{fills}")
            fill_k  = input("  Fill (default block):       ").strip() or 'block'
            fill_ch = g.FILL_CHARS.get(fill_k, '#')
            print(f"  Borders:   {borders}")
            border  = input("  Border (default fancy):     ").strip() or 'fancy'
            animate = input("  Typewriter reveal? [y/N]:   ").strip().lower() == 'y'
            g.generate_banner(text, color=color, border=border, fill=fill_ch,
                               gradient=grad, animate=animate)
            last_style = "banner"

        elif choice == '2':
            g.generate_wave(text, cycles=3)
            last_style = "wave"

        elif choice == '3':
            colors = [c for c in g.COLORS if c not in ('reset', 'bold', 'dim')]
            color  = input(f"  Color {colors} (default white): ").strip() or 'white'
            double = input("  Double border? [y/N]: ").strip().lower() == 'y'
            g.generate_box(text, color=color, double_border=double)
            last_style = "box"

        elif choice == '4':
            shadow_chars = {'block': '█', 'shade': '▓', 'light': '░', 'hash': '#'}
            sc_key = input(f"  Shadow char {list(shadow_chars.keys())} (default shade): ").strip() or 'shade'
            g.generate_shadow(text, shadow_char=shadow_chars.get(sc_key, '▓'))
            last_style = "shadow"

        elif choice == '5':
            bold = input("  Bold text? [y/N]: ").strip().lower() == 'y'
            g.generate_rainbow(text, bold=bold)
            last_style = "rainbow"

        elif choice == '6':
            colors = [c for c in g.COLORS if c not in ('reset', 'bold', 'dim')]
            fills  = list(g.FILL_CHARS.keys())
            color  = input(f"  Color {colors} (default cyan): ").strip() or 'cyan'
            fill_k = input(f"  Fill {fills} (default block): ").strip() or 'block'
            g.generate_stacked(text, fill=g.FILL_CHARS.get(fill_k, '█'), color=color)
            last_style = "stacked"

        elif choice == '7':
            colors = [c for c in g.COLORS if c not in ('reset', 'bold', 'dim')]
            color  = input(f"  Color {colors} (default green): ").strip() or 'green'
            g.generate_matrix(text, color=color)
            last_style = "matrix"

        elif choice == '8':
            g.generate_glitch(text)
            last_style = "glitch"

        elif choice == '9':
            colors = [c for c in g.COLORS if c not in ('reset', 'bold', 'dim')]
            color  = input(f"  Color {colors} (default yellow): ").strip() or 'yellow'
            g.generate_outline(text, color=color)
            last_style = "outline"

        else:
            print("⚠  Invalid choice — pick from the menu.")


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
ASCII Art Generator
Create cool text art with different styles!
"""

import random

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
            ' ': ['      ', '      ', '      ', '      ', '      ', '      '],
        }
    }
    
    COLORS = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'reset': '\033[0m'
    }
    
    BORDERS = {
        'stars': ('*' * 60, '*' * 60),
        'lines': ('=' * 60, '=' * 60),
        'fancy': ('╔' + '═' * 58 + '╗', '╚' + '═' * 58 + '╝'),
        'double': ('*' * 60, '*' * 60),
    }
    
    def generate_banner(self, text, color='cyan', border='stars'):
        """Generate ASCII art banner"""
        text = text.upper()
        lines = [''] * 6
        
        for char in text:
            if char in self.STYLES['banner']:
                char_lines = self.STYLES['banner'][char]
                for i in range(6):
                    lines[i] += char_lines[i] + ' '
        
        # Add color
        color_code = self.COLORS.get(color, '')
        reset_code = self.COLORS['reset']
        
        # Add border
        top_border, bottom_border = self.BORDERS.get(border, ('', ''))
        
        print(f"\n{color_code}{top_border}{reset_code}")
        for line in lines:
            print(f"{color_code}{line}{reset_code}")
        print(f"{color_code}{bottom_border}{reset_code}\n")
    
    def generate_wave(self, text):
        """Generate wavy text animation"""
        wave_chars = "~≈∿∼⋰⋱"
        for i in range(3):
            output = ""
            for j, char in enumerate(text):
                offset = (j + i) % len(wave_chars)
                output += f"{wave_chars[offset]} {char} "
            print(output)
    
    def generate_box(self, text):
        """Generate text in a box"""
        width = len(text) + 4
        top = '┌' + '─' * (width - 2) + '┐'
        middle = '│ ' + text + ' │'
        bottom = '└' + '─' * (width - 2) + '┘'
        
        print(f"\n{top}\n{middle}\n{bottom}\n")
    
    def generate_shadow(self, text):
        """Generate text with shadow effect"""
        print(f"\n{text}")
        shadow = ''.join(['▓' if c != ' ' else ' ' for c in text])
        print(f" {shadow}\n")
    
    def generate_rainbow(self, text):
        """Generate rainbow colored text"""
        colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
        output = ""
        for i, char in enumerate(text):
            color = colors[i % len(colors)]
            output += f"{self.COLORS[color]}{char}"
        output += self.COLORS['reset']
        print(f"\n{output}\n")

def display_menu():
    """Display the menu"""
    print("\n" + "="*50)
    print("🎨  ASCII ART GENERATOR  🎨")
    print("="*50)
    print("1. Banner Style (Big Letters)")
    print("2. Wave Effect")
    print("3. Box Frame")
    print("4. Shadow Effect")
    print("5. Rainbow Colors")
    print("6. Random Style")
    print("7. Exit")
    print("="*50)

def main():
    generator = AsciiArtGenerator()
    
    print("\n✨ Welcome to ASCII Art Generator! ✨")
    
    while True:
        display_menu()
        choice = input("\nChoose a style (1-7): ").strip()
        
        if choice == '7':
            print("\n👋 Thanks for using ASCII Art Generator! Goodbye!\n")
            break
        
        text = input("Enter your text: ").strip()
        
        if not text:
            print("Please enter some text!")
            continue
        
        if choice == '1':
            colors = list(generator.COLORS.keys())[:-1]
            color = input(f"Choose color {colors} (default: cyan): ").strip() or 'cyan'
            borders = list(generator.BORDERS.keys())
            border = input(f"Choose border {borders} (default: stars): ").strip() or 'stars'
            generator.generate_banner(text, color, border)
        
        elif choice == '2':
            generator.generate_wave(text)
        
        elif choice == '3':
            generator.generate_box(text)
        
        elif choice == '4':
            generator.generate_shadow(text)
        
        elif choice == '5':
            generator.generate_rainbow(text)
        
        elif choice == '6':
            # Random style
            style = random.choice([1, 2, 3, 4, 5])
            if style == 1:
                generator.generate_banner(text)
            elif style == 2:
                generator.generate_wave(text)
            elif style == 3:
                generator.generate_box(text)
            elif style == 4:
                generator.generate_shadow(text)
            else:
                generator.generate_rainbow(text)
        
        else:
            print("Invalid choice! Please choose 1-7.")

if __name__ == "__main__":
    main()
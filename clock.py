import os
import sys
import time
import datetime
import msvcrt

# Включаем поддержку UTF-8 и ANSI цветов / Enable UTF-8 and ANSI escape codes on Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
os.system('')

# ANSI коды управления экраном / Console control sequences
HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"
CURSOR_HOME = "\033[H"
CLEAR_SCREEN = "\033[2J"
COLOR_RESET = "\033[0m"

# 8 разных ASCII шрифтов для цифр / 8 distinct ASCII digit fonts
FONTS = {
    # 1. Blocks / Сплошные блоки
    1: {
        '0': ["███", "█ █", "█ █", "█ █", "███"],
        '1': ["  █", "  █", "  █", "  █", "  █"],
        '2': ["███", "  █", "███", "█  ", "███"],
        '3': ["███", "  █", "███", "  █", "███"],
        '4': ["█ █", "█ █", "███", "  █", "  █"],
        '5': ["███", "█  ", "███", "  █", "███"],
        '6': ["███", "█  ", "███", "█ █", "███"],
        '7': ["███", "  █", "  █", "  █", "  █"],
        '8': ["███", "█ █", "███", "█ █", "███"],
        '9': ["███", "█ █", "███", "  █", "███"],
        ':': ["   ", " █ ", "   ", " █ ", "   "]
    },
    # 2. Hash / Решетки
    2: {
        '0': ["###", "# #", "# #", "# #", "###"],
        '1': ["  #", "  #", "  #", "  #", "  #"],
        '2': ["###", "  #", "###", "#  ", "###"],
        '3': ["###", "  #", "###", "  #", "###"],
        '4': ["# #", "# #", "###", "  #", "  #"],
        '5': ["###", "#  ", "###", "  #", "###"],
        '6': ["###", "#  ", "###", "# #", "###"],
        '7': ["###", "  #", "  #", "  #", "  #"],
        '8': ["###", "# #", "###", "# #", "###"],
        '9': ["###", "# #", "###", "  #", "###"],
        ':': ["   ", " # ", "   ", " # ", "   "]
    },
    # 3. Stars / Звездочки
    3: {
        '0': ["***", "* *", "* *", "* *", "***"],
        '1': ["  *", "  *", "  *", "  *", "  *"],
        '2': ["***", "  *", "***", "*  ", "***"],
        '3': ["***", "  *", "***", "  *", "***"],
        '4': ["* *", "* *", "***", "  *", "  *"],
        '5': ["***", "*  ", "***", "  *", "***"],
        '6': ["***", "*  ", "***", "* *", "***"],
        '7': ["***", "  *", "  *", "  *", "  *"],
        '8': ["***", "* *", "***", "* *", "***"],
        '9': ["***", "* *", "***", "  *", "***"],
        ':': ["   ", " * ", "   ", " * ", "   "]
    },
    # 4. LCD Single-line / Одинарный LCD
    4: {
        '0': ["┌─┐", "│ │", "│ │", "│ │", "└─┘"],
        '1': ["  ┐", "  │", "  │", "  │", "  ┴"],
        '2': ["┌─┐", "  │", "┌─┘", "│  ", "└─┘"],
        '3': ["┌─┐", "  │", "┌─┤", "  │", "└─┘"],
        '4': ["│ │", "│ │", "└─┤", "  │", "  ┴"],
        '5': ["┌─┐", "│  ", "└─┐", "  │", "└─┘"],
        '6': ["┌─┐", "│  ", "├─┐", "│ │", "└─┘"],
        '7': ["┌─┐", "  │", "  │", "  │", "  ┴"],
        '8': ["┌─┐", "│ │", "├─┤", "│ │", "└─┘"],
        '9': ["┌─┐", "│ │", "└─┤", "  │", "└─┘"],
        ':': ["   ", " o ", "   ", " o ", "   "]
    },
    # 5. LCD Double-line / Двойной LCD
    5: {
        '0': ["╔═╗", "║ ║", "║ ║", "║ ║", "╚═╝"],
        '1': ["  ╗", "  ║", "  ║", "  ║", "  ╩"],
        '2': ["╔═╗", "  ║", "╔═╝", "║  ", "╚═╝"],
        '3': ["╔═╗", "  ║", "╔═╣", "  ║", "╚═╝"],
        '4': ["║ ║", "║ ║", "╚═╣", "  ║", "  ╩"],
        '5': ["╔═╗", "║  ", "╚═╗", "  ║", "╚═╝"],
        '6': ["╔═╗", "║  ", "╠═╗", "║ ║", "╚═╝"],
        '7': ["╔═╗", "  ║", "  ║", "  ║", "  ╩"],
        '8': ["╔═╗", "║ ║", "╠═╣", "║ ║", "╚═╝"],
        '9': ["╔═╗", "║ ║", "╚═╣", "  ║", "╚═╝"],
        ':': ["   ", " o ", "   ", " o ", "   "]
    },
    # 6. Dots / Точки
    6: {
        '0': ["●●●", "● ●", "● ●", "● ●", "●●●"],
        '1': ["  ●", "  ●", "  ●", "  ●", "  ●"],
        '2': ["●●●", "  ●", "●●●", "●  ", "●●●"],
        '3': ["●●●", "  ●", "●●●", "  ●", "●●●"],
        '4': ["● ●", "● ●", "●●●", "  ●", "  ●"],
        '5': ["●●●", "●  ", "●●●", "  ●", "●●●"],
        '6': ["●●●", "●  ", "●●●", "● ●", "●●●"],
        '7': ["●●●", "  ●", "  ●", "  ●", "  ●"],
        '8': ["●●●", "● ●", "●●●", "● ●", "●●●"],
        '9': ["●●●", "● ●", "●●●", "  ●", "●●●"],
        ':': ["   ", " ● ", "   ", " ● ", "   "]
    },
    # 7. Shaded / Штриховка
    7: {
        '0': ["▒▒▒", "▒ ▒", "▒ ▒", "▒ ▒", "▒▒▒"],
        '1': ["  ▒", "  ▒", "  ▒", "  ▒", "  ▒"],
        '2': ["▒▒▒", "  ▒", "▒▒▒", "▒  ", "▒▒▒"],
        '3': ["▒▒▒", "  ▒", "▒▒▒", "  ▒", "▒▒▒"],
        '4': ["▒ ▒", "▒ ▒", "▒▒▒", "  ▒", "  ▒"],
        '5': ["▒▒▒", "▒  ", "▒▒▒", "  ▒", "▒▒▒"],
        '6': ["▒▒▒", "▒  ", "▒▒▒", "▒ ▒", "▒▒▒"],
        '7': ["▒▒▒", "  ▒", "  ▒", "  ▒", "  ▒"],
        '8': ["▒▒▒", "▒ ▒", "▒▒▒", "▒ ▒", "▒▒▒"],
        '9': ["▒▒▒", "▒ ▒", "▒▒▒", "  ▒", "▒▒▒"],
        ':': ["   ", " ▒ ", "   ", " ▒ ", "   "]
    },
    # 8. Bulb Matrix / Ламповая матрица
    8: {
        '0': ["OOO", "O.O", "O.O", "O.O", "OOO"],
        '1': ["..O", "..O", "..O", "..O", "..O"],
        '2': ["OOO", "..O", "OOO", "O..", "OOO"],
        '3': ["OOO", "..O", "OOO", "..O", "OOO"],
        '4': ["O.O", "O.O", "OOO", "..O", "..O"],
        '5': ["OOO", "O..", "OOO", "..O", "OOO"],
        '6': ["OOO", "O..", "OOO", "O.O", "OOO"],
        '7': ["OOO", "..O", "..O", "..O", "..O"],
        '8': ["OOO", "O.O", "OOO", "O.O", "OOO"],
        '9': ["OOO", "O.O", "OOO", "..O", "OOO"],
        ':': ["...", " o ", "...", " o ", "..."]
    }
}

def parse_bool(val):
    return val.lower() in ('true', 'yes', '1', 'on')

def load_config():
    """
    Парсит конфиг config.txt со всеми расширенными настройками.
    Parses config.txt with all advanced settings keys.
    """
    color_map = {
        'green': (0, 255, 0),
        'red': (255, 0, 0),
        'blue': (0, 0, 255),
        'cyan': (0, 255, 255),
        'magenta': (255, 0, 255),
        'yellow': (255, 255, 0),
        'white': (255, 255, 255),
        'orange': (255, 127, 0),
        'purple': (128, 0, 128),
        'pink': (255, 192, 203),
    }
    
    # Значения по умолчанию / Default config values
    cfg = {
        'color': (0, 255, 255),
        'timezone': 3.0,
        'design': 'custom',
        'size': 'auto',
        'seconds': True,
        'format': '24h',
        'flash_colon': True,
        'fill_char': 'block',
        'show_date': True,
        'show_progress': True,
        'date_format': '%A, %d %B %Y',
        'custom_style': 1
    }
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, "config.txt")
    
    if os.path.exists(config_path):
        try:
            with open(config_path, "r", encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    
                    if '=' in line:
                        key, val = line.split('=', 1)
                        key = key.strip().lower()
                        val = val.strip()
                        
                        if key == 'color':
                            val_lower = val.lower()
                            is_hex = (val_lower.startswith('#') and len(val_lower) == 7 and 
                                      all(c in '0123456789abcdef' for c in val_lower[1:]))
                            if is_hex:
                                r = int(val_lower[1:3], 16)
                                g = int(val_lower[3:5], 16)
                                b = int(val_lower[5:7], 16)
                                cfg['color'] = (r, g, b)
                            elif val_lower in color_map:
                                cfg['color'] = color_map[val_lower]
                                
                        elif key == 'timezone':
                            val_clean = val.lower().replace('utc', '').replace('gmt', '').replace('+', '').strip()
                            try:
                                cfg['timezone'] = float(val_clean) if '-' not in val_clean else -float(val_clean.replace('-', ''))
                            except ValueError:
                                pass
                                
                        elif key == 'design':
                            val_lower = val.lower()
                            if val_lower in ('custom', 'peaclock', 'peacklock'):
                                cfg['design'] = 'peaclock' if val_lower in ('peaclock', 'peacklock') else 'custom'
                                
                        elif key == 'size':
                            val_lower = val.lower()
                            if val_lower == 'auto':
                                cfg['size'] = 'auto'
                            else:
                                try:
                                    cfg['size'] = int(val)
                                except ValueError:
                                    pass
                                    
                        elif key == 'seconds':
                            cfg['seconds'] = parse_bool(val)
                            
                        elif key == 'format':
                            val_lower = val.lower()
                            if val_lower in ('24h', '12h'):
                                cfg['format'] = val_lower
                                
                        elif key == 'flash_colon':
                            cfg['flash_colon'] = parse_bool(val)
                            
                        elif key == 'fill_char':
                            cfg['fill_char'] = val
                            
                        elif key == 'show_date':
                            cfg['show_date'] = parse_bool(val)
                            
                        elif key == 'show_progress':
                            cfg['show_progress'] = parse_bool(val)
                            
                        elif key == 'date_format':
                            cfg['date_format'] = val
                            
                        elif key == 'custom_style':
                            try:
                                val_int = int(val)
                                if 1 <= val_int <= 8:
                                    cfg['custom_style'] = val_int
                            except ValueError:
                                pass
        except Exception:
            pass
            
    return cfg

def get_time(offset):
    utc_now = datetime.datetime.now(datetime.timezone.utc)
    return utc_now + datetime.timedelta(hours=offset)

def get_time_string(time_now, show_seconds, is_24h):
    """
    Преобразует время в строковый формат в зависимости от 24h/12h и секунд.
    Converts time to standard string representation based on config format.
    """
    hour = time_now.hour
    is_pm = False
    
    if not is_24h:
        is_pm = hour >= 12
        hour = hour % 12
        if hour == 0:
            hour = 12
            
    min_val = time_now.minute
    sec_val = time_now.second
    
    if show_seconds:
        time_str = f"{hour:02d}:{min_val:02d}:{sec_val:02d}"
    else:
        time_str = f"{hour:02d}:{min_val:02d}"
        
    return time_str, is_pm

def calculate_block_size(width, height, size_cfg, grid_width, is_custom=False, show_date=True, show_progress=True):
    """
    Вычисляет размеры блока с учетом настроек высоты и ширины дашборда.
    Calculates responsive blocks ensuring bounds safety.
    """
    margin_y = 0
    if is_custom:
        margin_y += 2  # Рамка сверху + пробел
        margin_y += 1  # Пробел под часами
        if show_progress:
            margin_y += 1
        if show_date:
            margin_y += 1
        if show_progress or show_date:
            margin_y += 1  # Разделительный пробел
        margin_y += 1  # Рамка снизу
        
    margin_x = 4 if is_custom else 0
    
    max_h = max(1, height - margin_y)
    max_w = max(1, width - margin_x)
    
    if size_cfg == 'auto':
        bh = max_h // 5
        bw = max_w // grid_width
        
        # Сохраняем пропорцию 2:1 для красивых квадратных сегментов
        if bw > bh * 2:
            bw = bh * 2
        elif bw < bh * 2:
            bh = bw // 2
    else:
        bh = size_cfg
        bw = size_cfg * 2
        
    bw = max(1, bw)
    bh = max(1, bh)
    
    # Страховка от переполнения / Strict bounds checking
    while bh * 5 > max_h and bh > 1:
        bh -= 1
    while bw * grid_width > max_w and bw > 1:
        bw -= 1
        
    return bw, bh

def build_clock_grid(time_str, font, flash_colon, seconds_now):
    """
    Собирает сетку строковых представлений цифр времени.
    Builds the 5-row string list representing the clock layout.
    """
    colon_active = not (flash_colon and (seconds_now % 2 != 0))
    
    grid = [[] for _ in range(5)]
    for char in time_str:
        if len(grid[0]) > 0:
            # Spacer column between digits (width 1)
            for r in range(5):
                grid[r].append(" ")
                
        if char == ':':
            colon_template = font[':']
            for r in range(5):
                grid[r].append(colon_template[r] if colon_active else "   ")
        else:
            digit_template = font[char]
            for r in range(5):
                grid[r].append(digit_template[r])
                
    return grid

def render_scaled_row(row_strings, bw, style_num, color_fg, color_bg, use_bg_fill):
    """
    Масштабирует и раскрашивает одну строку символов сетки.
    Renders and scales characters for a single terminal row.
    """
    line_parts = []
    for s in row_strings:
        for char in s:
            if char == ' ':
                line_parts.append(" " * bw)
            elif char == '.':
                # Тусклые фоновые диоды для ламповой матрицы
                line_parts.append("\033[90m" + "." * bw + COLOR_RESET)
            else:
                # Рисуем активный блок: стилю 1 доступен сплошной фон, остальные рисуются текстом
                if style_num == 1 and use_bg_fill:
                    line_parts.append(color_bg + " " * bw + COLOR_RESET)
                else:
                    line_parts.append(color_fg + char * bw + COLOR_RESET)
    return "".join(line_parts)

def draw_peaclock(time_now, color_rgb, width, height):
    """
    Оригинальный адаптивный стиль peaclock без рамок.
    Всегда использует стандартные настройки peaclock: 24h, секунды, авторазмер и сплошные блоки.
    """
    time_str, _ = get_time_string(time_now, show_seconds=True, is_24h=True)
    
    # В peaclock всегда стиль 1 (блоки) и точки не мигают
    font = FONTS[1]
    grid_units = build_clock_grid(time_str, font, flash_colon=False, seconds_now=time_now.second)
    
    # Всегда авторазмер (grid_width = 31 для шрифта ширины 3 и 7 разделителей)
    bw, bh = calculate_block_size(width, height, 'auto', grid_width=31, is_custom=False)
    
    # Отрисовка
    color_bg = f"\033[48;2;{color_rgb[0]};{color_rgb[1]};{color_rgb[2]}m"
    color_fg = f"\033[38;2;{color_rgb[0]};{color_rgb[1]};{color_rgb[2]}m"
    
    lines = []
    for r in range(5):
        for _ in range(bh):
            line = render_scaled_row(grid_units[r], bw, 1, color_fg, color_bg, use_bg_fill=True)
            lines.append(line)
            
    # Центрирование
    padding_x = max(0, (width - (31 * bw)) // 2)
    padding_y = max(0, (height - (5 * bh)) // 2)
    
    centered_lines = []
    for _ in range(padding_y):
        centered_lines.append("")
    for line in lines:
        centered_lines.append(" " * padding_x + line)
        
    return "\n".join(centered_lines)

def draw_custom(time_now, cfg, width, height):
    """
    Ретро дашборд со всеми дополнительными виджетами и кастомным стилем шрифта.
    """
    time_str, is_pm = get_time_string(time_now, cfg['seconds'], cfg['format'] == '24h')
    
    # Получаем выбранный шрифт / Select font style
    style_num = cfg['custom_style']
    font = FONTS[style_num]
    
    grid_units = build_clock_grid(time_str, font, cfg['flash_colon'], time_now.second)
    
    grid_width = 31 if cfg['seconds'] else 19
    bw, bh = calculate_block_size(width, height, cfg['size'], grid_width, is_custom=True, 
                                  show_date=cfg['show_date'], show_progress=cfg['show_progress'])
    
    # Отрисовка больших цифр / Render digit segments
    color_bg = f"\033[48;2;{cfg['color'][0]};{cfg['color'][1]};{cfg['color'][2]}m"
    color_fg = f"\033[38;2;{cfg['color'][0]};{cfg['color'][1]};{cfg['color'][2]}m"
    use_bg_fill = (cfg['fill_char'].lower() == 'block')
    
    time_rows = []
    for r in range(5):
        for _ in range(bh):
            line = render_scaled_row(grid_units[r], bw, style_num, color_fg, color_bg, use_bg_fill)
            time_rows.append(line)
            
    box_width = grid_width * bw + 4
    
    # Форматирование даты
    try:
        date_str = time_now.strftime(cfg['date_format'])
    except Exception:
        date_str = time_now.strftime("%A, %d %B %Y")
        
    # Формирование шапки
    tz_sign = "+" if cfg['timezone'] >= 0 else ""
    tz_label = f"UTC{tz_sign}{cfg['timezone']}"
    ampm_label = f" [{ 'PM' if is_pm else 'AM' }]" if cfg['format'] == '12h' else ""
    title_text = f" WINCLOCK [{tz_label}]{ampm_label} "
    
    border_left_len = (box_width - len(title_text)) // 2
    border_right_len = box_width - len(title_text) - border_left_len
    
    top_border = "┌" + "─" * border_left_len + title_text + "─" * border_right_len + "┐"
    bottom_border = "└" + "─" * box_width + "┘"
    
    output = []
    output.append(top_border)
    output.append("│" + " " * box_width + "│")
    
    for row in time_rows:
        pad = (box_width - (grid_width * bw)) // 2
        line = "│" + " " * pad + row + " " * (box_width - (grid_width * bw) - pad) + "│"
        output.append(line)
        
    output.append("│" + " " * box_width + "│")
    
    if cfg['show_progress']:
        seconds = time_now.second
        percent = int((seconds / 59) * 100)
        percent_str = f" {percent}%"
        sec_str = f" ({seconds:02d}s)"
        prefix = "Progress: ["
        suffix = "]" + percent_str + sec_str
        
        # Резервируем отступы по бокам в 2 символа / Reserve 2 characters padding
        target_str_width = box_width - 4
        bar_width = target_str_width - len(prefix) - len(suffix)
        
        if bar_width < 5:
            # Упрощенная версия для небольших окон / Simplified version for small windows
            prefix = "Bar: ["
            suffix = f"] {percent}%"
            bar_width = target_str_width - len(prefix) - len(suffix)
            
            if bar_width < 5:
                # Минималистичный текстовый вывод для очень маленьких окон / Text fallback
                bar_str = f"Sec: {seconds:02d}s"
                bar_width = 0
                
        if bar_width > 0:
            filled = max(0, min(bar_width, int((seconds / 59) * bar_width)))
            bar = "█" * filled + "░" * (bar_width - filled)
            bar_str = prefix + bar + suffix
            
        bar_pad = (box_width - len(bar_str)) // 2
        output.append("│" + " " * bar_pad + color_fg + bar_str + COLOR_RESET + " " * (box_width - len(bar_str) - bar_pad) + "│")
        
    if cfg['show_date']:
        date_pad = (box_width - len(date_str)) // 2
        output.append("│" + " " * date_pad + date_str + " " * (box_width - len(date_str) - date_pad) + "│")
        
    if cfg['show_progress'] or cfg['show_date']:
        output.append("│" + " " * box_width + "│")
        
    output.append(bottom_border)
    
    # Центрирование
    centered_output = []
    padding_x = max(0, (width - box_width - 2) // 2)
    padding_y = max(0, (height - len(output)) // 2)
    
    for _ in range(padding_y):
        centered_output.append("")
    for line in output:
        centered_output.append(" " * padding_x + line)
        
    return "\n".join(centered_output)

def main():
    # Очистка и скрытие курсора / Clear terminal screen
    sys.stdout.write(CLEAR_SCREEN)
    sys.stdout.write(HIDE_CURSOR)
    sys.stdout.flush()
    
    cfg = load_config()
    prev_width, prev_height = 0, 0
    frame_count = 0
    
    try:
        while True:
            # Выход по кнопкам ESC, Q или Ctrl+C / Exit on ESC, Q or Ctrl+C
            if msvcrt.kbhit():
                ch = msvcrt.getch()
                if ch in (b'\x1b', b'q', b'Q', b'\x03'):
                    break
            
            # Читаем конфиг раз в секунду / Poll config updates
            frame_count += 1
            if frame_count % 10 == 0:
                cfg = load_config()
                
            # Получаем текущие размеры экрана / Fetch terminal sizes
            try:
                width, height = os.get_terminal_size()
            except Exception:
                width, height = 80, 25
                
            # Очищаем экран при ресайзе консоли / Clear screen on resize
            if width != prev_width or height != prev_height:
                sys.stdout.write(CLEAR_SCREEN)
                sys.stdout.flush()
                prev_width = width
                prev_height = height
                
            time_now = get_time(cfg['timezone'])
            
            if cfg['design'] == 'peaclock':
                frame = draw_peaclock(time_now, cfg['color'], width, height)
            else:
                frame = draw_custom(time_now, cfg, width, height)
                
            sys.stdout.write(CURSOR_HOME)
            sys.stdout.write(frame)
            sys.stdout.flush()
            
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        pass
    finally:
        # Восстановление консоли / Restore terminal state
        sys.stdout.write(CLEAR_SCREEN)
        sys.stdout.write(CURSOR_HOME)
        sys.stdout.write(SHOW_CURSOR)
        sys.stdout.flush()

if __name__ == '__main__':
    main()

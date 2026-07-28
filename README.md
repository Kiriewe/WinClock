# 🕒 winclock

**winclock** — это высоконастраиваемые консольные ASCII-часы для Windows, написанные на Python. Они поддерживают адаптивное изменение размера цифр, 8 встроенных ASCII-шрифтов, 12/24-часовые форматы, мигающие двоеточия, виджеты даты и полосы секунд, а также изменение настроек «на лету» без перезапуска программы.

**winclock** is a highly customizable console ASCII clock for Windows written in Python. It features responsive auto-sizing digit blocks, 8 built-in ASCII styles/fonts, 12/24-hour formats, flashing colons, custom calendar date cards, a seconds progress bar, and on-the-fly configuration updates without restarting the application.

---

## ✨ Особенности / Features

*   **8 стилей цифр / 8 digit styles**: От сплошных блоков до одинарных/двойных LCD-рамок, светодиодных точек и ретро-ламп (Bulb Matrix).
*   **Адаптивность / Responsive Auto-sizing**: Автоматически масштабирует размер цифр под размеры окна терминала, удерживая пропорцию 2:1 для красивого вида.
*   **Конфигурация «на лету» / Hot-reloading config**: Изменения в `config.txt` считываются каждую секунду во время работы программы.
*   **Секундный прогресс-бар / Seconds progress bar**: Динамический горизонтальный бар с защитой от переполнения границ экрана.
*   **Спектр цветов / Color Palette**: Полная поддержка Truecolor HEX-кодов и названий базовых цветов.

---

## 🚀 Запуск / Quick Start

1.  Убедитесь, что у вас установлен Python 3.
    Ensure you have Python 3 installed.
2.  Запустите часы через файл **`run.bat`** (или выполните команду `python clock.py` в консоли).
    Run the clock via **`run.bat`** (or execute `python clock.py` in your terminal).
3.  Для выхода из часов нажмите клавишу **`ESC`**, **`Q`** или **`Ctrl+C`**.
    To quit, press **`ESC`**, **`Q`**, or **`Ctrl+C`**.

---

## 🛠️ Настройка / Configuration (`config.txt`)

Вы можете настраивать внешний вид часов в файле `config.txt`:
You can configure the clock appearance in the `config.txt` file:

*   `color`: Базовый цвет (`cyan`, `green`, `red` и др.) или любой HEX-код цвета (например, `#FF5555`).
*   `timezone`: Смещение часового пояса относительно UTC (например, `+3` для Москвы, `-5` для Нью-Йорка).
*   `design`: Стиль отображения:
    *   `custom` (настраиваемый ретро-дашборд с рамкой, датой и шкалой секунд).
    *   `peaclock` (минималистичный безрамочный дизайн по подобию утилиты peaclock на Linux).
*   `size`: Размер блоков цифр: `auto` (автоподбор под размер консоли) или целое число (например, `1`, `2`, `3`).
*   `seconds`: Показывать или скрывать секунды (`true` / `false`).
*   `format`: Формат времени (`24h` / `12h` с AM/PM индикатором в шапке).
*   `flash_colon`: Мигание точек двоеточия каждую секунду (`true` / `false`).
*   `fill_char`: Символ заливки цифр: `block` (сплошная цветная заливка) или любой текст (например, `#` или `░`).
*   `show_date` / `show_progress`: Скрытие/показ календаря и прогресс-бара секунд.
*   `custom_style`: Выбор одного из 8 стилей шрифта (от `1` до `8`) для кастомного режима.

---

## 🎨 Цветовая палитра / Color Palette

В репозитории есть готовый файл **`hex_palette.md`**, который содержит более 100 красивых и гармоничных HEX-кодов, сгруппированных по темам. Используйте их в параметре `color` для быстрой настройки стиля!
There is a **`hex_palette.md`** file in the repository containing over 100 beautiful and harmonious HEX color codes sorted by theme. Use them in the `color` setting for quick personalization!

---

## 📄 Лицензия / License

Этот проект распространяется под свободной лицензией **MIT License**. Подробнее см. в файле `LICENSE`.
This project is licensed under the **MIT License** - see the `LICENSE` file for details.

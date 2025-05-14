import tkinter as tk

menu_options = [
    "Возобновить игру",
    "Новая игра",
    "Сохранить игру",
    "Загрузить игру",
    "Выход"
]

current_selection = 0
menu_window = None


def show_menu(game):
    global menu_window, current_selection
    if menu_window:
        return

    menu_window = tk.Toplevel()
    menu_window.title("Меню")
    menu_window.geometry("400x300")
    menu_window.grab_set()
    menu_window.bind('<Key>', lambda e: handle_menu_key(e, game))

    update_menu()


def update_menu():
    global menu_window
    for widget in menu_window.winfo_children():
        widget.destroy()
    for idx, option in enumerate(menu_options):
        color = "black" if idx != current_selection else "blue"
        label = tk.Label(menu_window, text=option, font=("Arial", 18), fg=color)
        label.pack(anchor="w", padx=20, pady=5)


def handle_menu_key(event, game):
    global current_selection, menu_window
    if event.keysym in ('w', 'Up'):
        current_selection = (current_selection - 1) % len(menu_options)
    elif event.keysym in ('s', 'Down'):
        current_selection = (current_selection + 1) % len(menu_options)
    elif event.keysym == 'Return':
        selected_option = menu_options[current_selection]
        if selected_option == "Возобновить игру":
            game.resume()
            menu_window.destroy()
        elif selected_option == "Новая игра":
            game.new_game()
            menu_window.destroy()
        elif selected_option == "Сохранить игру":
            game.save_game()
        elif selected_option == "Загрузить игру":
            game.load_game()
        elif selected_option == "Выход":
            game.root.quit()
    update_menu()

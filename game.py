import tkinter as tk
import menu
import pickle

WIDTH = 800
HEIGHT = 800
FINISH_LINE = WIDTH - 100


class BlockRaceGame:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='white')
        self.canvas.pack()

        self.red_x = 50
        self.blue_x = 50
        self.red = self.canvas.create_rectangle(self.red_x, 200, self.red_x + 50, 250, fill='red')
        self.blue = self.canvas.create_rectangle(self.blue_x, 400, self.blue_x + 50, 450, fill='blue')

        self.canvas.create_line(FINISH_LINE, 0, FINISH_LINE, HEIGHT, fill="black", width=3)

        self.is_paused = False
        self.game_running = True

        self.root.bind('<Key>', self.handle_key)
        self.root.protocol("WM_DELETE_WINDOW", self.root.quit)

    def handle_key(self, event):
        if not self.game_running:
            return

        if event.keysym == 'Escape':
            self.pause()
            menu.show_menu(self)
        elif not self.is_paused:
            if event.keysym == 'Right':  # изменено с 'z' на 'Right'
                self.move_red()
            elif event.keysym == 'd':
                self.move_blue()

    def move_red(self):
        self.canvas.move(self.red, 10, 0)
        self.red_x += 10
        self.check_winner()

    def move_blue(self):
        self.canvas.move(self.blue, 10, 0)
        self.blue_x += 10
        self.check_winner()

    def check_winner(self):
        if self.red_x + 50 >= FINISH_LINE:
            self.end_game("Красный победил!")
        elif self.blue_x + 50 >= FINISH_LINE:
            self.end_game("Синий победил!")

    def pause(self):
        self.is_paused = True

    def resume(self):
        self.is_paused = False

    def new_game(self):
        self.canvas.move(self.red, 50 - self.red_x, 0)
        self.canvas.move(self.blue, 50 - self.blue_x, 0)
        self.red_x = 50
        self.blue_x = 50
        self.resume()

    def save_game(self):
        with open("savegame.dat", "wb") as f:
            pickle.dump((self.red_x, self.blue_x), f)

    def load_game(self):
        try:
            with open("savegame.dat", "rb") as f:
                self.red_x, self.blue_x = pickle.load(f)
                self.canvas.coords(self.red, self.red_x, 200, self.red_x + 50, 250)
                self.canvas.coords(self.blue, self.blue_x, 400, self.blue_x + 50, 450)
        except FileNotFoundError:
            print("Сохранение не найдено.")

    def end_game(self, message):
        self.game_running = False
        self.canvas.create_text(WIDTH / 2, HEIGHT / 2, text=message, font=("Arial", 32), fill="green")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Гонка блоков")
    game = BlockRaceGame(root)
    root.mainloop()


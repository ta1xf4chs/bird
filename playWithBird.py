# นายตะวัน อุ้มชู 116410400029-7
import PySimpleGUI as sg
from PIL import Image

class BirdGUI:
    def __init__(self):
        self.birds = [
            Bird("Robina", 6, "C:/Users/ta1/Desktop/ta1Work/ta1py/test/Robina.png"),
            Bird("Eglen ", 8, "C:/Users/ta1/Desktop/ta1Work/ta1py/test/Eglen.png"),
            Bird("Stri  ", 7, "C:/Users/ta1/Desktop/ta1Work/ta1py/test/Stri.png"),
            Bird("Toccan", 5, "C:/Users/ta1/Desktop/ta1Work/ta1py/test/Toccan.png")
        ]

        layout = [
            [sg.Text("Select Bird:"), sg.OptionMenu(values=[bird.name for bird in self.birds], key='-BIRD-'), sg.Button("Ok")],
            [sg.Image(key='-BIRD_IMAGE-')],
            [sg.Text("Enter Bird's Message:"), sg.InputText(key='-MESSAGE-')],
            [sg.Button("Make Bird Talk"), sg.Button("Show History"), sg.Button("Clear History")],  # เพิ่มปุ่ม "Clear History" ที่นี่
            [sg.Multiline("", size=(50, 10), key='-OUTPUT-')]
        ]
        self.window = sg.Window("Bird Chat(ENGLISH ONLY!!)", layout)

    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "Ok":
                selected_bird_name = values['-BIRD-']
                selected_bird = next((bird for bird in self.birds if bird.name == selected_bird_name), None)
                self.window['-BIRD_IMAGE-'].update(filename=selected_bird.image_path)
            elif event == "Make Bird Talk":
                selected_bird_name = values['-BIRD-']
                selected_bird = next((bird for bird in self.birds if bird.name == selected_bird_name), None)
                message = values['-MESSAGE-']
                if message:
                    selected_bird.talk(message)
                    self.window['-OUTPUT-'].update(f"{selected_bird.name} says: {message}")
                    self.save_to_file(selected_bird, message)
                else:
                    self.window['-OUTPUT-'].update(f"{selected_bird.name} is {selected_bird.age} years old.")
                    self.save_to_file(selected_bird, f"{selected_bird.name} is {selected_bird.age} years old.")
                self.window['-BIRD_IMAGE-'].update(filename=selected_bird.image_path)
            elif event == "Show History":
                history = self.read_from_file()
                self.window['-OUTPUT-'].update(history)
            elif event == "Clear History":  # เพิ่มส่วนนี้เพื่อลบประวัติ
                self.clear_history()

    def clear_history(self):
        with open("bird_messages_history.txt", "w") as file:
            file.write("")  # เขียนข้อความว่างไปยังไฟล์ bird_messages_history.txt เพื่อลบประวัติทั้งหมด
        self.window['-OUTPUT-'].update("History cleared.")  # แสดงข้อความบอกว่าประวัติถูกลบ


    def save_to_file(self, bird, message):
        with open("bird_messages_history.txt", "a") as file:
            file.write(f"{bird.name} says: {message}\n")
    def read_from_file(self):
        try:
            with open("bird_messages_history.txt", "r") as file:
                history = file.readlines()
            history_text = "".join(history)
        except FileNotFoundError:
            history_text = "CAN'T FIND HISTORY!!!"
        return history_text


class Bird:
    def __init__(self, name, age, image_path):
        self.name = name
        self.age = age
        self.image_path = image_path
    def talk(self, message):
        print(f"{self.name} says: {message}")


if __name__ == "__main__":
    app = BirdGUI()
    app.run()

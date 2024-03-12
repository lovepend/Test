import tkinter as tk
from tkinter import filedialog
import threading
import pyautogui
import time

class App:
    def __init__(self, master):
        self.master = master
        master.title('그림 파일 찾기 및 순서 조정 프로그램')

        self.image_paths = []
        self.search_threads = []
        self.stop_event = threading.Event()

        self.listbox = tk.Listbox(master, width=100, height=10)
        self.listbox.pack(pady=10)

        self.add_button = tk.Button(master, text="이미지 추가", command=self.add_image)
        self.add_button.pack()

        self.delete_button = tk.Button(master, text="이미지 삭제", command=self.delete_image)
        self.delete_button.pack()

        self.move_up_button = tk.Button(master, text="위로 이동", command=self.move_up)
        self.move_up_button.pack()

        self.move_down_button = tk.Button(master, text="아래로 이동", command=self.move_down)
        self.move_down_button.pack()

        self.start_button = tk.Button(master, text="찾기 시작", command=self.start_search)
        self.start_button.pack()

    def add_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image_paths.append(file_path)
            self.listbox.insert(tk.END, file_path)

    def delete_image(self):
        try:
            selected_index = self.listbox.curselection()[0]
            self.image_paths.pop(selected_index)
            self.listbox.delete(selected_index)
        except IndexError:
            print("삭제할 이미지를 선택해주세요.")

    def move_up(self):
        try:
            selected_index = self.listbox.curselection()[0]
            if selected_index > 0:
                # 리스트에서 위치 변경
                self.image_paths.insert(selected_index-1, self.image_paths.pop(selected_index))
                # UI에서 위치 변경
                self.listbox.insert(selected_index-1, self.listbox.get(selected_index))
                self.listbox.delete(selected_index+1)
                self.listbox.select_set(selected_index-1)
        except IndexError:
            print("이동할 이미지를 선택해주세요.")

    def move_down(self):
        try:
            selected_index = self.listbox.curselection()[0]
            if selected_index < len(self.image_paths) - 1:
                # 리스트에서 위치 변경
                self.image_paths.insert(selected_index+1, self.image_paths.pop(selected_index))
                # UI에서 위치 변경
                self.listbox.insert(selected_index+2, self.listbox.get(selected_index))
                self.listbox.delete(selected_index)
                self.listbox.select_set(selected_index+1)
        except IndexError:
            print("이동할 이미지를 선택해주세요.")

    def find_image(self, image_path):
        while not self.stop_event.is_set():
            location = pyautogui.locateCenterOnScreen(image_path, confidence=0.8)
            if location:
                pyautogui.click(location)
                print(f"{image_path} 찾아 클릭함.")
                break  # 이미지를 찾고 클릭했으면 해당 이미지에 대한 검색 중지
            else:
                print(f"{image_path} 찾는 중...")
                time.sleep(1)  # 찾을 때까지 계속 시도

    def start_search(self):
        self.stop_event.clear()
        for path in self.image_paths:
            t = threading.Thread(target=self.find_image, args=(path,))
            t.start()
            self.search_threads.append(t)
            t.join()  # 이전 이미지에 대한 검색이 완료될 때까지 기다림

if __name__ == "__main__":
    root = tk.Tk()
    my_app = App(root)
    root.mainloop()

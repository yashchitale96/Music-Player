from pygame import mixer
from tkinter import *
from tkinter import filedialog, messagebox

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x400")
        self.root.title("Music Player")
        mixer.init()

        self.current_file = StringVar()

        # Create frames
        top_frame = Frame(root)
        top_frame.pack(pady=20)

        middle_frame = Frame(root)
        middle_frame.pack(pady=20)

        bottom_frame = Frame(root)
        bottom_frame.pack()

        # Labels
        Label(top_frame, text="Welcome to Music Player", font="lucida 18 bold").pack()

        Label(middle_frame, text="Select a File:", font="lucida 12").grid(row=0, column=0, padx=10)
        Entry(middle_frame, textvariable=self.current_file, width=40).grid(row=0, column=1, padx=10)
        Button(middle_frame, text="Choose File", command=self.choose_file).grid(row=0, column=2, padx=10)

        # Buttons
        Button(bottom_frame, text="Play", command=self.play).pack(side=LEFT, padx=10)
        Button(bottom_frame, text="Pause", command=self.pause).pack(side=LEFT, padx=10)
        Button(bottom_frame, text="Resume", command=self.resume).pack(side=LEFT, padx=10)
        Button(bottom_frame, text="Stop", command=self.stop).pack(side=LEFT, padx=10)
        Button(bottom_frame, text="Quit", command=self.root.destroy).pack(side=LEFT, padx=10)

    def play(self):
        try:
            mixer.music.load(self.current_file.get())
            mixer.music.play()
        except pygame.error:
            messagebox.showerror("Error", "Failed to load or play the selected file.")

    def pause(self):
        mixer.music.pause()

    def resume(self):
        mixer.music.unpause()

    def stop(self):
        mixer.music.stop()

    def choose_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            self.current_file.set(file_path)

if __name__ == "__main__":
    root = Tk()
    app = MusicPlayer(root)
    root.mainloop()

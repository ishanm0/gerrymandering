import tkinter as tk


class ToggleAdvancedButton(tk.Button):
    def __init__(self, parameter_panel):
        self.parameter_panel = parameter_panel
        self.shown = False
        font = 'Consolas 8 underline'
        super().__init__(parameter_panel, command=self.toggle, font=font, text='Show advanced ▼', borderwidth=0)
        self.pack(side='top', pady=(10, 0))

        self.bind('<Button-1>', self.mouse_down)
        self.bind('<ButtonRelease-1>', self.mouse_up)

    def mouse_down(self, _):
        self.config(fg='gray')
        return 'break'

    def mouse_up(self, _):
        self.config(fg='black')
        self.toggle()

    def toggle(self):
        self.pack_forget()
        for adjuster in self.parameter_panel.adjusters.values():
            if adjuster.advanced:
                if self.shown:
                    adjuster.frame.pack_forget()
                else:
                    adjuster.pack()
        self.shown = not self.shown
        if self.shown:
            self.parameter_panel.button_frame.pack(side='top')
        else:
            self.parameter_panel.button_frame.pack_forget()
        self.pack(side='top', pady=(10, 0))
        self.config(text='Hide advanced ▲' if self.shown else 'Show advanced ▼')
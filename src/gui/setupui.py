import tkinter as tk
from tkinter import filedialog, messagebox, ttk, font as tkfont

from src.gui.modern_progress_bar import ModernProgressBar
from src.gui.modern_widgets import ModernButton
from src.gui.icon import Icon
from src.gui.language_settings import language_options_window
from src.version import get_version

# Import localization manager
from src.localization import get_localized

class SetupUI:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        self.icon = Icon(self.master)
        self.language_window = language_options_window(self.master)
        self.entries = {}
        self.buttons = {}
        self.progress = None
        self.console = None
        self.timer_label = None
        self.status_label = None

    def setup_ui(self):
        # Create main content frame
        main_frame = ttk.Frame(self.master, padding="40 40 40 40", style="TFrame")
        main_frame.grid(row=0, column=0, sticky="nsew")
        
        # Configure grid weights for expansion
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

        # Configure main frame grid weights
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(3, weight=1)  # Make console expand

        self.create_project_path_inputs(main_frame)
        self.create_buttons(main_frame)
        self.create_console(main_frame)
        self.create_progress_bar(main_frame)
        self.create_info_labels(main_frame)

        # Set minimum window size
        self.master.minsize(600, 400)

    def create_project_path_inputs(self, parent):
        paths = [("GameMaker", self.app.browse_gm, self.icon.get_gamemaker_icon()),
                ("Godot", self.app.browse_godot, self.icon.get_godot_icon())]
       
        for idx, (label, command, icon) in enumerate(paths):
            Game_Engine = get_localized(f"Menu_{label}")
            frame = ttk.Frame(parent, style="TFrame")
            frame.grid(row=idx, column=0, columnspan=3, sticky="ew", pady=(0, 20))
            
            icon_label = ttk.Label(frame, text=label[:2] if icon is None else "", image=icon, style="TLabel")
            icon_label.pack(side=tk.LEFT, padx=(0, 10))

            path_label = ttk.Label(frame, text=get_localized("Menu_UI_Directory_Heading").format(Game_Engine = Game_Engine), style="TLabel")
            path_label.pack(side=tk.LEFT)
            
            entry = ttk.Entry(frame, style="TEntry")
            entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10)
            
            browse_button = ModernButton(frame, text=get_localized("Menu_UI_Directory_Button").format(Game_Engine = Game_Engine), command=command)
            browse_button.pack(side=tk.LEFT)
            
            self.entries[label.lower()] = entry

    def create_buttons(self, parent):
        button_frame = ttk.Frame(parent, style="TFrame")
        button_frame.grid(row=2, column=0, columnspan=3, pady=(0, 30), sticky="ew")
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(2, weight=1)

        # Create inner frame for buttons to center them
        inner_button_frame = ttk.Frame(button_frame, style="TFrame")
        inner_button_frame.grid(row=0, column=1)

        # Create convert and settings buttons
        convert_button = ModernButton(inner_button_frame, text=get_localized("Menu_UI_Button_Convert"), command=self.app.start_conversion)
        convert_button.grid(row=0, column=0, padx=10)
        self.buttons[get_localized("Menu_UI_Button_Convert")] = convert_button

        # Create stop button with icon
        stop_button = ModernButton(inner_button_frame, command=self.app.stop_conversion, state=tk.DISABLED, icon_only=True)
        stop_icon = ModernButton.create_stop_icon(inner_button_frame, size=24)
        stop_button.configure(image=stop_icon)
        stop_button._icon = stop_icon  # Keep a reference to prevent garbage collection
        stop_button.grid(row=0, column=1, padx=10)
        self.buttons[get_localized("Menu_UI_Button_Stop")] = stop_button

        settings_button = ModernButton(inner_button_frame, text=get_localized("Menu_UI_Button_Settings"), command=self.app.open_settings)
        settings_button.grid(row=0, column=2, padx=10)
        self.buttons[get_localized("Menu_UI_Button_Settings")] = settings_button

    def get_button(self, button_name):
        return self.buttons.get(button_name)

    def create_console(self, parent):
        console_frame = ttk.Frame(parent, style="TFrame")
        console_frame.grid(row=3, column=0, columnspan=3, sticky="nsew", pady=(0, 20))
        console_frame.grid_columnconfigure(0, weight=1)
        console_frame.grid_rowconfigure(0, weight=1)

        self.console = tk.Text(console_frame, 
                             wrap=tk.WORD, 
                             bg="#2d2d2d", 
                             fg="#e0e0e0", 
                             insertbackground="#e0e0e0", 
                             font=('Cascadia Code', 10), 
                             state='disabled',
                             padx=10,
                             pady=10,
                             relief="flat",
                             borderwidth=0)
        self.console.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(console_frame, 
                                orient="vertical", 
                                command=self.console.yview, 
                                style="Console.Vertical.TScrollbar")
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.console.configure(yscrollcommand=scrollbar.set)

    def create_progress_bar(self, parent):
        progress_frame = ttk.Frame(parent, style="TFrame")
        progress_frame.grid(row=4, column=0, columnspan=3, sticky="ew", pady=(0, 10))
        progress_frame.grid_columnconfigure(0, weight=1)

        self.progress = ModernProgressBar(progress_frame, 
                                        width=0,  # Let it expand
                                        height=30, 
                                        bg_color="#2d2d2d", 
                                        fill_color="#0078d4", 
                                        text_color="#ffffff")
        self.progress.grid(row=0, column=0, sticky="ew")

        status_frame = ttk.Frame(parent, style="TFrame")
        status_frame.grid(row=5, column=0, columnspan=3, pady=(0, 20), sticky="ew")
        status_frame.grid_columnconfigure(1, weight=1)
        
        self.timer_label = ttk.Label(status_frame, 
                                   text=f"{get_localized('Menu_UI_Time_Heading')} 00:00:00", 
                                   style="TLabel",
                                   font=('Segoe UI', 10))
        self.timer_label.grid(row=0, column=0, padx=(0, 20))

        self.status_label = ttk.Label(status_frame, 
                                    text="", 
                                    style="TLabel",
                                    font=('Segoe UI', 10))
        self.status_label.grid(row=0, column=1, sticky="w")

    def create_info_labels(self, parent):
        info_frame = ttk.Frame(parent, style="TFrame")
        info_frame.grid(row=6, column=0, columnspan=3, sticky="ew")
        info_frame.grid_columnconfigure(1, weight=1)

        version_label = ttk.Label(info_frame, 
                                text=get_localized("UI_Label_Version").format(version=get_version()), 
                                style="TLabel", 
                                cursor="hand2",
                                font=('Segoe UI', 9))
        version_label.grid(row=0, column=0, padx=10)
        version_label.bind("<Button-1>", self.app.show_release_notes)
        version_label.bind('<Enter>', lambda e: version_label.configure(foreground="#0078d4"))
        version_label.bind('<Leave>', lambda e: version_label.configure(foreground="#e0e0e0"))

        contribute_label = ttk.Label(info_frame, 
                                   text=get_localized("UI_Label_Contribute"), 
                                   style="TLabel", 
                                   cursor="hand2",
                                   font=('Segoe UI', 9))
        contribute_label.grid(row=0, column=1, padx=10)
        contribute_label.bind("<Button-1>", self.app.open_github)
        contribute_label.bind('<Enter>', lambda e: contribute_label.configure(foreground="#0078d4"))
        contribute_label.bind('<Leave>', lambda e: contribute_label.configure(foreground="#e0e0e0"))

        made_by_label = ttk.Label(info_frame, 
                                text=get_localized("UI_Label_MadeBy"), 
                                style="TLabel", 
                                cursor="hand2",
                                font=('Segoe UI', 9))
        made_by_label.grid(row=0, column=2, padx=10)
        made_by_label.bind("<Button-1>", self.app.open_infiland_website)
        made_by_label.bind('<Enter>', lambda e: made_by_label.configure(foreground="#0078d4"))
        made_by_label.bind('<Leave>', lambda e: made_by_label.configure(foreground="#e0e0e0"))

        language_options_label = ttk.Label(info_frame,
                                image=self.icon.get_language_icon(),
                                style="TLabel",
                                cursor="hand2")
        language_options_label.grid(row=0, column=3, padx=10)
        language_options_label.bind("<Button-1>", self.language_window.open_window)

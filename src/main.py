from src.gui.mainWindow import MainWindow
from src.functionality.binder import Binder
from src.functionality.startup.startup import Startup


main_window = MainWindow("Deductions", "900x650")

Startup.initialize()
Binder.bind()

main_window.mainloop()


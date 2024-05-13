from src.gui.guiTracking.guiTracker import GUITracker


class Applications:
    @staticmethod
    def cmd_applications_main_page():
        menu = GUITracker.get("men_applications")
        notebook = GUITracker.get("multi_tab_main_page")

        for i in range(menu.index("end") + 1):
            if menu.entrycget(i, "label") == "Main":
                menu.entryconfigure(i, command=lambda: notebook.lift())
                break

    @staticmethod
    def cmd_applications_retirement_utils():
        menu = GUITracker.get("men_applications")
        notebook = GUITracker.get("multi_tab_retirement_utils")

        for i in range(menu.index("end") + 1):
            if menu.entrycget(i, "label") == "Retires utils":
                menu.entryconfigure(i, command=lambda: notebook.lift())
                break

    @staticmethod
    def cmd_applications_backup():
        menu = GUITracker.get("men_applications")
        notebook = GUITracker.get("frm_backup")

        for i in range(menu.index("end") + 1):
            if menu.entrycget(i, "label") == "Backup":
                menu.entryconfigure(i, command=lambda: notebook.lift())
                break
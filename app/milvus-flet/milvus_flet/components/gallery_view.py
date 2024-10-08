import flet as ft

from .controls_grid import ControlsGrid
from .examples_view import ExamplesView
from .left_navigation_menu import LeftNavigationMenu


class GalleryView(ft.Row):
    def __init__(self, gallery):
        super().__init__()
        self.gallery = gallery
        self.left_nav = LeftNavigationMenu(gallery)
        self.controls_grid = ControlsGrid(gallery)
        self.examples_view = ExamplesView(gallery)
        self.expand = True
        self.controls = [
            self.left_nav,
            ft.VerticalDivider(width=1),
            self.controls_grid,
            self.examples_view,
        ]

    def display_controls_grid(self):
        self.controls_grid.display()
        self.examples_view.examples.controls = []
        self.examples_view.visible = False
        self.page.update()

    def display_control_examples(self, control_name):
        self.examples_view.display(
            self.gallery.get_control(
                self.gallery.selected_control_group.name, control_name
            )
        )
        self.controls_grid.visible = False
        self.page.update()
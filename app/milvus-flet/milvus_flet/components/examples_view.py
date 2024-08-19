import os
from pathlib import Path
from typing import List
import flet as ft


class ExamplesView(ft.Column):
    def __init__(self, gallery):
        super().__init__()
        self.gallery = gallery
        self.visible = False
        self.expand = True
        self.control_name_text = ft.Text(style=ft.TextThemeStyle.HEADLINE_MEDIUM)
        self.control_description = ft.Text(style=ft.TextThemeStyle.BODY_MEDIUM)
        self.examples = ft.Column(expand=True, spacing=10, scroll=ft.ScrollMode.AUTO)
        self.controls = [
            self.control_name_text,
            self.control_description,
            self.examples,
        ]
        self.logo_path = os.path.join(
            str(Path(__file__).parent.parent), "assets", "github-mark.svg"
        )

    def display(self, grid_item):
        self.visible = True
        self.examples.controls = []
        self.control_name_text.value = grid_item.name
        self.control_description.value = grid_item.description

        for example in grid_item.examples:
            containsViews: List[ft.Control] = []
            if example.name:
                containsViews.append(
                    ft.Container(
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Text(
                                    example.name,
                                    style=ft.TextThemeStyle.TITLE_MEDIUM,
                                    weight=ft.FontWeight.W_500,
                                ),
                                ft.IconButton(
                                    content=ft.Image(
                                        src=self.logo_path,
                                        width=24,
                                        height=24,
                                        color=ft.colors.ON_SURFACE,
                                    ),
                                    url="https://github.com/SimFG/mua",
                                    url_target="_blank",
                                ),
                            ],
                        ),
                        bgcolor=ft.colors.SECONDARY_CONTAINER,
                        padding=5,
                        border_radius=5,
                    ),
                )
            containsViews.append(
                ft.Container(
                    content=example.example(),
                    clip_behavior=ft.ClipBehavior.NONE,
                ),
            )
            self.examples.controls.append(
                ft.Column(
                    controls=containsViews,
                )
            )
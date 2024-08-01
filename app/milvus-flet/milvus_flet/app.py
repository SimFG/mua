import logging
import os
from pathlib import Path

import flet as ft
import flet.version

from milvus_flet.components.gallery_view import GalleryView
from milvus_flet.gallerydata import GalleryData

gallery = GalleryData()

logging.basicConfig(level=logging.INFO)


def core(page: ft.Page):
    page.title = "Milvus tool gallery"

    def get_route_list(route):
        route_list = [item for item in route.split("/") if item != ""]
        return route_list

    def route_change(e):
        route_list = get_route_list(page.route)

        if len(route_list) == 0:
            # HINT: which is the first route
            page.go("/counter")
        else:
            gallery.selected_control_group = gallery.get_control_group(route_list[0])
            if len(route_list) == 1:
                gallery_view.display_controls_grid()
            elif len(route_list) == 2:
                gallery_view.display_control_examples(route_list[1])
            else:
                print("Invalid route")

    gallery_view = GalleryView(gallery)
    logo_path = os.path.join(
            str(Path(__file__).parent), "assets", "logo.svg"
        )

    page.appbar = ft.AppBar(
        leading=ft.Container(padding=5, content=ft.Image(src=logo_path)),
        leading_width=40,
        title=ft.Text("Milvus tool gallery"),
        center_title=True,
        bgcolor=ft.colors.INVERSE_PRIMARY,
        actions=[
            ft.Container(
                padding=10, content=ft.Text(f"Flet version: {flet.version.version}")
            )
        ],
    )

    page.theme_mode = ft.ThemeMode.LIGHT
    page.on_error = lambda e: print("Page error:", e.data)

    page.add(gallery_view)
    page.on_route_change = route_change
    print(f"Initial route: {page.route}")
    page.go(page.route)

def main():
    ft.app(core)

if __name__ == "__main__":
    main()
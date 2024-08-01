from flet import IconButton, Row, TextField, icons

name = "Basic counter example"


def example():
    txt_number = TextField(value="0", text_align="right", width=100)

    async def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        await txt_number.update_async()

    async def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        await txt_number.update_async()

    return Row(
            [
                IconButton(icons.REMOVE, on_click=minus_click),
                txt_number,
                IconButton(icons.ADD, on_click=plus_click),
            ],
            alignment="center",
        )
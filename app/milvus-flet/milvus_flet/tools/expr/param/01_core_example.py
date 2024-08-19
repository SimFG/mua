import httpx
from flet import Text, Column, TextField, ElevatedButton

def example():
    expr_port = 9091
    async def button_clicked(e):
        async with httpx.AsyncClient() as client:
            url = f"{milvus_address.value}:{expr_port}/expr?auth={root_path.value}&code={expr_code.value}"
            resp = await client.get(url)
            expr_result.value = resp.text
            await expr_result.update_async()

    milvus_address = TextField(label="milvus address", value="http://localhost", suffix_text=f":{expr_port}")
    root_path = TextField(label="root path", value="by-dev")
    expr_code = TextField(label="expr code", value="rootcoord.address")
    b = ElevatedButton(text="submit", on_click=button_clicked)
    expr_result = Text()

    return Column(
            [
                milvus_address,
                root_path,
                expr_code,
                b,
                expr_result,
            ],
        )
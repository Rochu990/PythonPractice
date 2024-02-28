from fastapi import FastAPI
from typing import Optional
from converters import from_binary_to_decimal_converter, from_decimal_to_binary_converter


app = FastAPI()

@app.put("/converter")
async def number_converter(bin: int | None = None, decimal: int | None = None):
    if decimal is not None:
        return from_decimal_to_binary_converter(decimal)
    if bin is not None:
        return from_binary_to_decimal_converter(bin)
    
    
import sys
from typing import BinaryIO, Union

__all__ = ["Error", "encode", "decode"]

_File = Union[str, BinaryIO]

class Error(Exception): ...

if sys.version_info >= (3, 7):
    def encode(
        in_file: _File, out_file: _File, name: str | None = ..., mode: int | None = ..., *, backtick: bool = ...
    ) -> None: ...

else:
    def encode(in_file: _File, out_file: _File, name: str | None = ..., mode: int | None = ...) -> None: ...

def decode(in_file: _File, out_file: _File | None = ..., mode: int | None = ..., quiet: int = ...) -> None: ...

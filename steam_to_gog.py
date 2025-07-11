import os
import uuid

header: str = open("header").read()

size = os.stat("FILE").st_size
size_string = str(size)

header = header[:300] + size_string.ljust(10, ' ') + header[310:]
header = header[:212] + size_string.ljust(10, '\n') + header[222:]

with open(str(uuid.uuid4()), "wb") as new_file:
    new_file.write(str.encode(header))
    with open("FILE", "rb") as source:
        processed: int = 0
        while processed < size:
            buffer = source.read(min(512, size - processed))
            processed += len(buffer)
            new_file.write(buffer)
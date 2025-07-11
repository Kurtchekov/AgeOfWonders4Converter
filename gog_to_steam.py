import os
from uuid import UUID

def is_valid_uuid(uuid_string):
    try:
        UUID(uuid_string)
        return True
    except ValueError:
        return False

for file in os.listdir("."):
    if not is_valid_uuid(file):
        continue

    size = os.stat(file).st_size

    with open("FILE", "wb") as new_file:
        with open(file, "rb") as source:
            processed: int = 0
            ignored: int = 0
            while processed < size:
                buffer = source.read(min(256, size - processed))
                processed += len(buffer)
                to_ignore = 312 - ignored
                if to_ignore >= len(buffer):
                    ignored += len(buffer)
                    continue
                buffer = buffer[to_ignore:]
                ignored += to_ignore
                new_file.write(buffer)
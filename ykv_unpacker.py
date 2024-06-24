import os
import json
from urllib.parse import unquote

def read_last_bytes(file_path, num_bytes):
    with open(file_path, 'rb') as f:
        f.seek(-num_bytes, 2)
        return f.read()

def unpack_files(packed_file, output_folder):
    last_16_bytes = read_last_bytes(packed_file, 16)
    size_info = last_16_bytes.decode('utf-8').strip()

    size_to_skip = int(size_info.split('\x00')[0].strip())

    with open(packed_file, 'rb') as f:
        f.seek(-(16 + size_to_skip), 2)
        json_data = f.read(size_to_skip)

    decoded_json = unquote(json_data.decode('utf-8'))
    files_info = json.loads(decoded_json)

    info_file_path = os.path.join(output_folder, 'info.json')
    with open(info_file_path, 'w', encoding='utf-8') as info_f:
        json.dump(files_info, info_f, indent=2)

    with open(packed_file, 'rb') as packed_f:
        for file_info in files_info:
            filename = file_info['name']
            offset = file_info['offset']
            size = file_info['size']

            packed_f.seek(offset)
            content = packed_f.read(size)

            if filename.endswith('.ts') or filename.endswith('.flv') or filename.endswith('.mp4'):
                content = content[34:]  # Skip the first 34 bytes

            output_path = os.path.join(output_folder, filename)
            with open(output_path, 'wb') as out_f:
                out_f.write(content)

            print(f'Extracted: {filename}')

def main():
    file_path = input("Enter the path to .ykv file: ").strip()
    output_folder = input("Enter the path to output folder: ").strip()

    os.makedirs(output_folder, exist_ok=True)

    unpack_files(file_path, output_folder)

if __name__ == "__main__":
    main()

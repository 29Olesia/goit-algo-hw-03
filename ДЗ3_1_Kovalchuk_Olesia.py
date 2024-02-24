import os
import shutil
import argparse

def copy_files(source_dir, dest_dir='dist'):
    try:
        os.makedirs(dest_dir, exist_ok=True)
       
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                file_extension = os.path.splitext(file)[1][1:].lower()
                destination_path = os.path.join(dest_dir, file_extension)
                os.makedirs(destination_path, exist_ok=True)
                destination_file_path = os.path.join(destination_path, file)

                shutil.copy(file_path, destination_file_path)
                print(f"Файл '{file}' скопійовано до '{destination_file_path}'")

    except Exception as e:
        print(f"Помилка: {e}")

def main():
    parser = argparse.ArgumentParser(description='Рекурсивна програма для копіювання та сортування файлів.')
    
    parser.add_argument('source_dir', help='Шлях до вихідної директорії')
    parser.add_argument('--dest_dir', default='dist', help='Шлях до директорії призначення (за замовчуванням "dist")')

    args = parser.parse_args()

    source_dir = args.source_dir
    dest_dir = args.dest_dir

    copy_files(source_dir, dest_dir)

if __name__ == "__main__":
    main()

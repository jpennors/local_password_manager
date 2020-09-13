from typing import Dict, TextIO
from modules.files.file_mode import FileMode


class FileManager:
    
    file_name = 'files.txt'

    @staticmethod
    def get_file_for_reading() -> TextIO:
        return FileManager.open_file(FileMode.READ_MODE)

    @staticmethod
    def get_file_for_updating() -> TextIO:
        return FileManager.open_file(FileMode.TRUNCATE_MODE)

    @staticmethod
    def create_file() -> TextIO:
        return FileManager.open_file(FileMode.TRUNCATE_MODE)

    @staticmethod
    def open_file(file_mode: FileMode) -> TextIO:
        return open(FileManager.file_name, FileManager.map_file_mode(file_mode))

    FILE_MODE_MAPPING: Dict[FileMode, str] = {
        FileMode.READ_MODE: 'r',
        FileMode.TRUNCATE_MODE: 'w'
    }

    @staticmethod
    def map_file_mode(file_mode: FileMode) -> str:
        return FileManager.FILE_MODE_MAPPING[file_mode]


import abc
from abc import ABC


class File(metaclass=abc.ABCMeta):
    def __init__(self, content):
        self.content = content

    def create(self):
        pass

    @abc.abstractmethod
    def clear(self):
        pass


class PdfFile(File, ABC):
    def __init__(self, content):
        super().__init__(content)

    def create(self):
        return print("PDF FILE CREATED")

    def clear(self):
        return print("CLEAR PDF")


class ExcelFile(File, ABC):
    def __init__(self, content, columns):
        super().__init__(content)
        self.columns = columns

    def create(self):
        print("EXCEL COLUMNS: ", self.columns)
        return print("EXCEL FILE CREATED: ", self.content)

    def clear(self):
        print("EXCEL COLUMNS: ", self.columns)
        return print("CLEAR EXCEL: ", self.content)


class TxtFile(File, ABC):
    def __init__(self, content, columns):
        super().__init__(content)
        self.columns = columns

    def create(self):
        print("TXT COLUMNS: ", self.columns)
        return print("TXT FILE CREATED: ", self.content.split(','))

    def clear(self):
        print("TXT COLUMNS: ", self.columns)
        return print("TXT EXCEL: ", self.content)


class FileFactory:
    def generate_file(self, file_type="PDF"):
        """Factory Method"""
        if file_type.upper() == 'PDF':
            content = input("Enter the pdf content: ")
            return PdfFile(content)

        elif file_type.upper() == 'EXCEL':
            content = input("Enter the excel content: ")
            columns = input("Enter the number of columns: ")
            return ExcelFile(content, int(columns))

        elif file_type.upper() == 'TXT':
            content = input("Enter the txt content: ")
            columns = input("Enter the number of columns: ")
            return TxtFile(content, int(columns))


if __name__ == "__main__":
    file_factory = FileFactory()
    file = file_factory.generate_file(input("Enter the type of the file (PDF, EXCEL, TXT): "))
    if not file:
        print("FILE TYPE NOT FOUND")
    else:
        print(f"The type of object created: {type(file)}")
        file.create()

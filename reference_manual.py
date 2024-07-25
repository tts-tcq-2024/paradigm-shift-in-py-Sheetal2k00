from color_code import get_color_from_pair_number

class ReferenceManual:
    def __init__(self):
        self.header = "25-Pair Color Code Reference Manual"
        self.separator = "-" * 33
        self.entries = self.generate_entries()

    def generate_entries(self):
        entries = []
        for i in range(1, 26):
            major, minor = get_color_from_pair_number(i)
            entries.append(f"{i}: {major} {minor}")
        return entries

    def print_manual(self):
        print(self.header)
        print(self.separator)
        for entry in self.entries:
            print(entry)

if __name__ == "__main__":
    manual = ReferenceManual()
    manual.print_manual()

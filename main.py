import os

BASE_PATH = os.getcwd()
RECEIPT_FILE_NAME = "receipts.txt"

full_path = os.path.join(BASE_PATH, RECEIPT_FILE_NAME)


with open(full_path, "r") as file:
    result = {}
    lines = []
    for line in file:
        data = lines.append(file.readline())
    print(lines)
        # if line is str:
        #     lines.append(file.readline())
        #     print(lines)
        # else:
        #     print("[e")
    #         quantity = int(line)
    #         pass
    #
    #     for item in range(quantity):
    #         data = file.readline().strip()
    #         lines.append(data)
    # print(result)

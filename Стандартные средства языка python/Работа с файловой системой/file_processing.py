# Вам дается текстовый файл, содержащий некоторое количество непустых строк. На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

lines = open("input.txt").readlines()
with open("output.txt", "w") as out:
    out.writelines(reversed(lines))
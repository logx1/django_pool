def line_to_dict(line):
    line = line.strip("\n")
    periodic_case = {}
    new_line = line.split("=")

    periodic_case['element'] = new_line[0]
    periodic_case[new_line[1].split(",")[0].split(":")[0]] = new_line[1].split(",")[0].split(":")[1]
    periodic_case[new_line[1].split(",")[1].split(":")[0]] = new_line[1].split(",")[1].split(":")[1]
    periodic_case[new_line[1].split(",")[2].split(":")[0]] = new_line[1].split(",")[2].split(":")[1]
    periodic_case[new_line[1].split(",")[3].split(":")[0]] = new_line[1].split(",")[3].split(":")[1]
    periodic_case[new_line[1].split(",")[4].split(":")[0]] = new_line[1].split(",")[4].split(":")[1]
    # print(periodic_case)
    return periodic_case

def read_file(file):
    periodic_table = []
    with open(file, "r") as fd:
        for line in fd:
            elem_dict = line_to_dict(line)
            if elem_dict:
                periodic_table.append(elem_dict)
    return periodic_table

def periodic_table_to_html(periodic_table):
    html = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Periodic Table</title>
<style>
body { font-family: Arial, sans-serif; margin: 20px; }
.periodic-grid {
    display: grid;
    grid-template-columns: repeat(18, 60px);
    grid-auto-rows: 80px;
    gap: 5px;
}
.element {
    border: 1px solid #333;
    padding: 5px;
    text-align: center;
    font-size: 12px;
    background-color: #f2f2f2;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.element span.symbol { font-size: 18px; font-weight: bold; }
.element span.number { font-size: 10px; color: #555; }
</style>
</head>
<body>
<h1>Periodic Table</h1>
<div class="periodic-grid">
"""
    for elem in periodic_table:
        col = int(elem.get('position', 0)) + 1  # Grid column starts from 1
        html += f'<div class="element" style="grid-column:{col}">'
        html += f'<span class="symbol">{elem.get("small","")}</span>'
        html += f'<span class="number">{elem.get("number","")}</span>'
        html += f'<span class="name">{elem.get("element","")}</span>'
        html += f'<span class="molar">{elem.get("molar","")}</span>'
        html += f'</div>\n'

    html += "</div>\n</body>\n</html>"
    return html

if __name__ == "__main__":
    table = read_file("periodic_table.txt")
    html_content = periodic_table_to_html(table)

    with open("periodic_table.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("Periodic table HTML file created as 'periodic_table.html'.")

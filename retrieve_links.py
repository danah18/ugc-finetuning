import re

with open("creative-milkshake/beauty.html", "r", encoding="utf-8") as f:
    content = f.read()

matches = re.findall(r'https:\/\/r2\.foreplay\.co[^\s"\'>]*', content)
with open("creative-milkshake/beauty-links.txt", "w") as file:
    for url in matches:
        file.write(url + "\n")

# Read the file
with open("creative-milkshake/beauty-links.txt", "r") as file:
    lines = file.readlines()

# Remove duplicates while preserving order
seen = set()
unique_lines = []
for line in lines:
    line = line.strip()
    if line and line not in seen:
        seen.add(line)
        unique_lines.append(line)

# Write back the unique lines
with open("creative-milkshake/beauty-links.txt", "w") as file:
    for line in unique_lines:
        file.write(line + "\n")

print("Duplicates removed. Cleaned file saved.")

print("Done.")
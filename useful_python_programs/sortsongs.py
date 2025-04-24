
with open('music\__tno_soundtrack.txt', 'r') as f:
    lines = f.readlines()

def sort_key(block):
    for line in block:
        if 'song' in line:
            parts = line.split('=')
            if len(parts) > 1:
                return parts[1].strip()
            else:
                return "" 
    return ""

blocks = []
current_block = []
for line in lines:
    if 'music' in line:
        if current_block:
            blocks.append(current_block)
            current_block = []
    current_block.append(line)
blocks.append(current_block) 

sorted_blocks = sorted(blocks, key=lambda x: sort_key(x))

sorted_lines = [line for block in sorted_blocks for line in block]

with open('music\__tno_soundtrack.txt', 'w') as f:
    f.writelines(sorted_lines)
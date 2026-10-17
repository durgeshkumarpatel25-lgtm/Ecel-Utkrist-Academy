with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    for i, line in enumerate(f):
        if 'banner' in line.lower() or 'uca' in line.lower() or 'poster' in line.lower():
            print(f"{i+1}: {line.strip()[:100]}")

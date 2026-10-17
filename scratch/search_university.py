with open('index.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if 'university' in line.lower() or 'raman' in line.lower() or 'cvru' in line.lower():
            safe = line.strip().encode('ascii', 'replace').decode('ascii')
            print(f"{i+1}: {safe[:120]}")

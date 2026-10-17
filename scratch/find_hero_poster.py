with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    for i, line in enumerate(f):
        if 'tap to zoom' in line.lower() or 'daily mic practice' in line.lower() or 'stage confidence' in line.lower():
            safe = line.strip().encode('ascii', 'replace').decode('ascii')
            print(f"{i+1}: {safe[:120]}")

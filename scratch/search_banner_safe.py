import sys

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    for i, line in enumerate(f):
        if 'banner' in line.lower() or 'banner2' in line.lower() or 'banner3' in line.lower():
            # encode safely
            safe_line = line.strip().encode('ascii', 'replace').decode('ascii')
            print(f"{i+1}: {safe_line[:120]}")

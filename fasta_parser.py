def parse_fasta(filepath):
    records = {}
    current_id = None
    current_seq = []
    
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if current_id is not None:
                    records[current_id] = len("".join(current_seq))
                current_id = line[1:]
                current_seq = []
            else:
                current_seq.append(line)
                
    if current_id is not None:
        records[current_id] = len("".join(current_seq))
        
    return records
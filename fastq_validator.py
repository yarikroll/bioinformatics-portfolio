def validate_fastq(path):
    record_num = 0
    
    with open(path) as f:
        while True:
            name = f.readline()
            if not name: 
                break
                
            record_num += 1
            seq = f.readline()
            wall = f.readline()
            qual = f.readline()
            
            if not (seq and wall and qual):
                raise ValueError(f"Record {record_num}: truncated file")
                
            name, seq, wall, qual = (s.strip() for s in (name, seq, wall, qual))
            
            if not name.startswith("@"):
                raise ValueError(f"Record {record_num}: missing @")
            if not wall.startswith("+"):
                raise ValueError(f"Record {record_num}: missing +")
            if len(seq) != len(qual):
                raise ValueError(f"Record {record_num}: length mismatch")
                
    return record_num


def create_sq():
    q = []
    si = 0

    def size():
        global q
        return len(q) - si

    def push(v):
        global q
        q.append(v)
        
    def popp():
        global q
        global si
        
        if size() == 0:
            return None
        
        v = q[si]
        si += 1
        
        if si > (len(q) / 2):
            q = q[si:]
            si = 0
            
        return v
    
    return {
        'size': size,
        'push': push,
        'pop': popp
    }
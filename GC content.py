def calculate_gc_content(sequence):
    sequence=("GCATGCATGCAT")
    count_g=0

    for ch in sequence:
        if ch == 'G':
            count+=1
        if ch == 'C':
            count+=1
    gc_content=(count/len(sequence))*100
    return gc_content

result=calculate_gc_content("ATGCATGCATGC")
print("GC_content", result)



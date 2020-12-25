def getCount(line):
    elemnts_count = dict()
    for i in line:
        elemnts_count[i]='1' if(not i in elemnts_count) else str(int(elemnts_count[i])+1)
    return elemnts_count

def getReduce(count1,count2):
    for key,val in count2.items():
        count1[key]=val if(not key in count1) else str(int(count1[key])+int(val))
    return count1

def getCountElements(lines):
    all_elements ={}
    for i in lines.split('\n'):
        getReduce(all_elements,getCount(i))
    return all_elements





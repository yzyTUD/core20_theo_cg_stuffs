import re
teststring = "helloworld hhh test wowo"
def word_count(file_name):
    import collections
    word_freq = collections.defaultdict(int)
    with open(file_name) as f:
        for l in f:
            for w in l.strip().split():  
                word_freq[w] += 1
    return word_freq
def regtest(file_name):
    mlist = []
    with open(file_name) as f:
        txt = f.read().replace('\n', '')
    x = re.search("wo", txt)
    print(x.start())
    cur = -1
    while x != None:
        cur = cur + 1 + x.start()
        x = re.search("wo", txt[cur+1:])
        if x != None:
            print(cur+1 + x.start())
    return mlist
def extractp(file_name):
    resulttxtlist = []
    with open(file_name,encoding='utf-8') as f:
        #for linetxt in f:
        #linetxt = f.readline():
            #print(linetxt)
            #if len(linetxt) > 80:
            #linetxt
            #resulttxtlist.append(linetxt)
        line = f.readline()
        cnt = 1
        while line:
            #print("Line {}: {}".format(cnt, len(line)))
            #line = line.lstrip()
            if len(line) > 76:
                resulttxtlist.append("\t" + line[0:76])
                resulttxtlist.append("\n\t" + line[76:])
            else:
                resulttxtlist.append("\t" + line)
            line = f.readline()
            cnt += 1
    #print(resulttxtlist)
    with open("pdf_mixed.txt","w",encoding='utf-8') as fout:
        for l in resulttxtlist:
            fout.write(l)
extractp("mixed.txt")

#split()
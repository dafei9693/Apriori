from utils import if_same,getSubsets,get_count

class Apriori():
    def __init__(self,data,min_sup,min_conf):
        self.data=data
        self.min_sup=min_sup
        self.min_conf=min_conf
        self.last_temp_list = []
        self.last_temp_sups = []
        self.temp_list=[]
        self.temp_sups=[]
        self.count = 1
        self.frequent_subset = 0

    def log(self):
        print('temp_list',self.temp_list)
        print('temp_sup',self.temp_sups)

    def initList(self):
        for i in self.data:
            for j in i:
                if j not in self.temp_list:
                    self.temp_list.append(j)

        for i in range(len(self.temp_list)):
            self.temp_sups.append(0)

    def get_sup(self):
        for i in self.temp_list:
            if type(i)==list:
                for j in self.data:
                    if_in = 0
                    for ii in range(len(i)):
                        if i[ii] in j:
                            if ii==len(i)-1:
                                if_in=1
                        else:
                            break
                    if if_in:
                        self.temp_sups[self.temp_list.index(i)] = self.temp_sups[self.temp_list.index(i)]+1

            else:
                for m in self.data:
                    for n in m:
                        if n==i:
                            self.temp_sups[self.temp_list.index(n)] = self.temp_sups[self.temp_list.index(n)] +1

    def prune(self):
        new_list = []
        new_sups = []
        for i in range(len(self.temp_sups)):
            if self.temp_sups[i]<self.min_sup:
                continue
            else:
                new_list.append(self.temp_list[i])
                new_sups.append(self.temp_sups[i])
        self.temp_sups = new_sups
        self.temp_list = new_list

    def getNew(self):
        new = []
        for i in range(len(self.temp_sups)):
            for j in range(i+1,len(self.temp_sups)):
                temp_new = []
                temp_new.append(self.temp_list[i])
                temp_new.append(self.temp_list[j])
                if temp_new not in new:
                    new.append(temp_new)

        if self.count>2:
            new1 = []
            for i in new:
                temp_new = []
                for j in i:
                    if type(j) == list:
                        for m in j:
                            if m not in temp_new:
                                temp_new.append(m)

                if len(temp_new) != self.count:
                    continue
                if_continue = 0
                for item in new1:
                    if if_same(item,temp_new):
                        if_continue=1
                if if_continue:
                    continue

                new1.append(temp_new)


        self.last_temp_list = self.temp_list
        self.last_temp_sups = self.temp_sups
        self.max_sup = max(self.temp_sups)
        self.temp_list = new
        if self.count>2:
            self.temp_list = new1
        self.temp_sups=[]
        for i in range(len(self.temp_list)):
            self.temp_sups.append(0)

    def getResult(self):
        print('\n\nresult')
        result = []
        h = []
        e = []
        conf = []
        for i in self.frequent_subset:
            subsets = getSubsets(i)
            for i in subsets:
                for j in subsets:

                    if i == j:
                        continue

                    if_continue = 0
                    for xx in range(len(i)):
                        if i[xx] in j:
                            if_continue=1
                    if if_continue:
                        continue

                    if len(i) == len(j) and i!=j:
                        continue

                    else:
                        confidence = get_count(j,self.data)/get_count(i,self.data)
                        if confidence>1:
                            confidence = 1
                        if confidence>self.min_conf:
                            h.append(i)
                            e.append(j)
                            conf.append(confidence)
                            print(i,"=>",j,"confidence:",confidence)

        result.append(h)
        result.append(e)
        result.append(conf)

        return result


    def demo(self):
        self.initList()
        self.get_sup()
        self.log()
        while self.min_sup<= max(self.temp_sups):
            self.count = self.count+1
            self.prune()
            print('after prune')
            self.log()
            self.frequent_subset = self.temp_list
            self.getNew()
            print('after concat')
            self.log()
            self.get_sup()
            print('after count')
            self.log()
            print('\n\n')

    def getFrequentSubset(self):
        return self.frequent_subset



from Apriori import Apriori

apri = Apriori([['l1','l2','l5'],['l2','l4'],['l2','l3'],['l1','l2','l4'],['l1','l3'],['l2','l3'],['l1','l3'],['l1','l2','l3','l5'],['l1','l2','l3']],2,0.7)
apri.demo()
print('frequentSubsets')
print(apri.getFrequentSubset())
apri.getResult()
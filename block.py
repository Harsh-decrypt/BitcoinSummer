txn_id=[]       #this is a list to store all the transaction ids in the mempool
ptxn_id=[]      #this stores all the Parent transaction ids
sum=0

#this is code given to us as an example in the question, build the logic on that

class MempoolTransaction():
    def __init__(self, txid, fee, weight, parents):
        self.txid = txid
        txn_id.append(txid)
        """Added a check to see whether the parent tx_id exists or not if not then the parent list is appended with a 0 otherwise it is appended with the parent id"""
        if parents is None:
            ptxn_id.append(0)
        else:
            ptxn_id.append(parents)
        self.fee = int(fee)
        self.weight = int(weight)
        ptxn=[]         #this holds all the unconfirmed parent transaction ids
        txn=[]          #this holds all the valid transaction ids
        """Logic for appending all valid transactions and all unconfirmed parent tx ids"""
        if parents not in txn_id[0:len(ptxn_id)]:
            ptxn.append(parents)
        else:
            txn.append(txid)
            global sum
            sum+=self.weight        #calculating total weight of block
        """Writing all the valid transactions to block.txt"""
        with open("block.txt", "a") as b:
            if sum<=4000000:
                for p in txn:
                    b.write(p)
                    b.write("\n")
            else:
                print("Not a Valid Block")



"""given with question as example it parses the mempool.csv and returns an instance of class MempoolTransaction and runs from 1 to the last"""
def parse_mempool_csv():
    with open('mempool.csv') as f:
        return([MempoolTransaction(*line.strip().split(',')) for line in f.readlines()[1:]])


parse_mempool_csv()         #calling the parsing function

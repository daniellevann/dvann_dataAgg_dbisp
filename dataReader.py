import pandas as pd
sample1 = "Sample_1.txt"
# read Sample1.txt, seperate into columns, add column names 
data1 = pd.read_csv(sample1, sep='|', header= None, names=["Stock Status", "Qty Avail All Branches", "Rebate Flag", "Rebate End Date", "D&H Item Number", "ManuF Item Number","UPC","Subcategory Code","Vendor Name","Unit Cost", "Rebate Amount", "Handling Charge", "Freight", "Ship Via","Weight","Short Description", "Long Description"])
# apply cost discount
data1["Unit Cost"] = data1["Unit Cost"]/(1-.15)
sample2 = "Sample_2.txt"
# read Sample_2.txt, seperate columns, rename and apply headers 
data2 = pd.read_csv(sample2, sep='~',header=None, )
d2 = data2.rename({0:'Trading Partner Code',1:'Detail Record ID',2:'Manufacturer Part #',3:'Internal Use',4:'SKU #',5:'Status Code',6:'Part Description',7:'Manufacturer Name',8:'Qty on Hand (total)',20:'Unit Cost'}, axis='columns')

# apply cost discount
data2[20] = data2[20]/(1-.18)

# print table
cols = ["Trading Partner Code", "Detail Record ID", "Manufacturer Part #", "Internal Use", "SKU #", "Status Code","Part Description", "Manufacturer Name", "Qty on Hand (total)","Unit Cost"]
dt2 = d2[cols]

sample3 = "Sample_3.txt"
# read Sample_3.txt, sperate columns, apply col names
data3 = pd.read_csv(sample3, sep=',')
# apply cost discount
data3["CustBestPrice"]=data3["CustBestPrice"]/(1-.12)

dataSets = [data1,dt2,data3]
totalData = lambda left,right: pd.merge(left,right,on=["Manufacturer Name"],how='outer'), dataSets

print(totalData)
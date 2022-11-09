import json

with open('baby.json') as f:
  datas = json.load(f)

for data in datas:
    print(data)
    print(f" data rading (productNumber) => {data['productNumber']}")
    print(f" data rading (productAsin) => {data['productAsin']}")
    print(f" data rading (productUuid) => {data['productUuid']}")
    print(f" data rading (productImageLink) => {data['productImageLink']}")
    print(f" data rading (productLink) => {data['productLink']}")
    print(f" data rading (productTitle) => {data['productTitle']}")
    print(f" data rading (productStar) => {data['productStar']}")
    print(f" data rading (CommentNumber) => {data['CommentNumber']}")
    print(f" data rading (productPrice) => {data['productPrice']}")
    print(f" data rading (productOldPrice) => {data['productOldPrice']}")
    print(f" data rading (discountRate) => {data['discountRate']}") 
    

import bs4, requests

def getProductPrize(productURL):
    res = requests.get(productURL, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"
});
    res.raise_for_status();

    soup = bs4.BeautifulSoup(res.text, "html.parser");
    elems = soup.select('#priceblock_ourprice');
    
    if len(elems) == 0:
        elems = soup.select('#priceblock_saleprice');

    productName = soup.select('#productTitle');
    return (elems[0].text.strip(), productName[0].text.strip());


print ("Enter Amazon Product URL : ")
price, productName = getProductPrize(input())
print ("The price of " + productName +" is : " + price)

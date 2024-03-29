from bs4 import BeautifulSoup
import requests
import streamlit as st
import pandas as pd
import time
data_ec = []

# def make_clickable(val):
#     return '<a href="{}" target="_blank">{}</a>'.format(val,val)

###SLC###
def get_data_SLC():
    url = 'https://slcbd.thebase.in/categories/3788862'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    item_list = soup.find_all('li', {'class': 'items-grid_itemListLI_5a0255a1'})
    for item in item_list:
        data_SLC ={}
        title = item.find('p', {'class': 'items-grid_itemTitleText_5a0255a1'}).text
        data_SLC['title'] = title
        price = item.find('p', {'class': 'items-grid_price_5a0255a1'}).text
        price = price.replace('¥', '').replace(',', '')
        price = int(price)
        data_SLC['price'] = price
        if '1ml' in title:
            data_SLC['capacity'] = '1ml'
        elif '0.5ml' in title:
            data_SLC['capacity'] = '0.5ml'
        else:
            data_SLC['capacity'] = '不明'
        
        stock = item.find('p', {'class': 'items-grid_soldOut_5a0255a1'}) == None
        data_SLC['stock'] = '在庫あり' if stock == True else 'SOLD OUT'
        
        if data_SLC['capacity'] == '1ml':
            data_SLC['0.1mlあたりの値段'] = price / 10
        elif data_SLC['capacity'] == '0.5ml':
            data_SLC['0.1mlあたりの値段'] = price / 5
        else:
            data_SLC['0.1mlあたりの値段'] = 0
        
        data_SLC['URL'] = item.find('a', {'class': 'items-grid_anchor_5a0255a1 js-anchor'})['href']
        data_ec.append(data_SLC)

###city420###################################################################################
def get_data_city420():
    url = 'https://city420.base.shop/'

    res = requests.get(url)

    soup = BeautifulSoup(res.text, 'html.parser')

    item_list = soup.find('ul', {'class': 'product_list row'})

    items = item_list.find_all('li')

    for item in items:
        data_city420 = {}
        title = item.find('h2', {'class': 'show_on_hover'}).text
        title = ''.join(title.split())
        data_city420['title'] = title
        price = int(item.find('div', {'class': 'price'}).text.replace('¥', '').replace(',', ''))
        data_city420['price'] = price
        if '1ml' in title:
            data_city420['capacity'] = '1ml'
        elif '0.5ml' in title:
            data_city420['capacity'] = '0.5ml'
        else:
            data_city420['capacity'] = '不明'

        stock = item.find('p', {'class': 'endOfSale'}) == None
        data_city420['stock'] = '在庫あり' if stock == True else 'SOLD OUT'
        
        if data_city420['capacity'] == '1ml':
            data_city420['0.1mlあたりの値段'] = price / 10
        elif data_city420['capacity'] == '0.5ml':
            data_city420['0.1mlあたりの値段'] = price / 5
        else:
            data_city420['0.1mlあたりの値段'] = 0
        
        data_city420['URL'] = item.find('a')['href']
        data_ec.append(data_city420)
    
###マカロニCBD/macaroniCBD#########################################
def get_data_macaroniCBD():
    url = 'https://macaronicbd.base.shop/categories/3317383'

    res = requests.get(url)

    soup = BeautifulSoup(res.text, 'html.parser')

    item_list = soup.find('div', {'class': 'c-items__list'})
    items = item_list.find_all('a')
    for item in items:
        data_macaroni = {}
        data_macaroni['title'] = item.find('div', {'class': 'c-card__name'}).text
        price = item.find('div', {'class': 'c-card__price'}).text
        price = price.replace('¥', '').replace(',', '')
        price = int(price)
        data_macaroni['price'] = price
        title = item.find('div', {'class': 'c-card__name'}).text
        if '1ml' in title:
            data_macaroni['capacity'] = '1ml'
        elif '0.5ml' in title:
            data_macaroni['capacity'] = '0.5ml'
        else:
            data_macaroni['capacity'] = '0.5ml'

        stock = item.find('span', {'class': 'c-card__tag endOfSale'}) == None
        data_macaroni['stock'] = '在庫あり' if stock == True else 'SOLD OUT'
        
        if data_macaroni['capacity'] == '1ml':
            data_macaroni['0.1mlあたりの値段'] = price / 10
        elif data_macaroni['capacity'] == '0.5ml':
            data_macaroni['0.1mlあたりの値段'] = price / 5
        else:
            data_macaroni['0.1mlあたりの値段'] = 0
        
        data_macaroni['URL'] = item.get('href')
        data_ec.append(data_macaroni)

    ##商品ページ2番目#######################################################################################

    url = 'https://macaronicbd.base.shop/load_items/categories/3317383/2'

    res = requests.get(url)

    soup = BeautifulSoup(res.text, 'html.parser')
    item_list = soup.find_all('a', {'class': 'c-card'})
    for item in item_list:
        data_macaroni = {}
        data_macaroni['title'] = item.find('div', {'class': 'c-card__name'}).text
        price = item.find('div', {'class': 'c-card__price'}).text
        price = price.replace('¥', '').replace(',', '')
        price = int(price)
        data_macaroni['price'] = price
        title = item.find('div', {'class': 'c-card__name'}).text
        if '1ml' in title:
            data_macaroni['capacity'] = '1ml'
        elif '0.5ml' in title:
            data_macaroni['capacity'] = '0.5ml'
        else:
            data_macaroni['capacity'] = '0.5ml'

        stock = item.find('span', {'class': 'c-card__tag endOfSale'}) == None
        data_macaroni['stock'] = '在庫あり' if stock == True else 'SOLD OUT'
                
        if data_macaroni['capacity'] == '1ml':
            data_macaroni['0.1mlあたりの値段'] = price / 10
        elif data_macaroni['capacity'] == '0.5ml':
            data_macaroni['0.1mlあたりの値段'] = price / 5
        else:
            data_macaroni['0.1mlあたりの値段'] = 0
            
        data_macaroni['URL'] = item.get('href')
        data_ec.append(data_macaroni)
        
###CBDSHOPまどろみ########
def get_data_madoromi():
    url = 'https://madoromicbd.thebase.in/categories/3194863'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    item_list = soup.find('ul', {'id': 'itemList'})
    items = item_list.find_all('li', {'class', 'items-grid_itemListLI_5a0255a1'})  

    for item in items:
        data_madoromi = {}
        data_madoromi['title'] = item.find('p', {'class': 'items-grid_itemTitleText_5a0255a1'}).text
        price = item.find('p', {'class': 'items-grid_price_5a0255a1'}).text
        price = price.replace('¥', '').replace(',', '')
        price = int(price)
        data_madoromi['price'] = price
        data_madoromi['capacity'] = '不明'
        stock = item.find('p', {'class': 'items-grid_soldOut_5a0255a1'}) == None
        data_madoromi['stock'] = '在庫あり' if stock == True else 'SOLD OUT'
        
        if data_madoromi['capacity'] == '1ml':
            data_madoromi['0.1mlあたりの値段'] = price / 10
        elif data_madoromi['capacity'] == '0.5ml':
            data_madoromi['0.1mlあたりの値段'] = price / 5
        else:
            data_madoromi['0.1mlあたりの値段'] = 0
        
        url = item.find('a')['href']
        data_madoromi['URL'] = url
        data_ec.append(data_madoromi)
        
###AncientCBD#####
def get_data_ancient():
    url = 'https://kajitsumanbo.thebase.in/categories/4038882'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    items = soup.find_all('li', {'class': 'items-grid_itemListLI_5a0255a1'})

    for item in items:
        data_ancientCBD = {}
        data_ancientCBD['title'] = item.find('p', {'class': 'items-grid_itemTitleText_5a0255a1'}).text
        price = item.find('p', {'class': 'items-grid_price_5a0255a1'}).text
        price = price.replace('¥', '').replace(',', '')
        price = int(price)
        data_ancientCBD['price'] = price
        title = item.find('p', {'class': 'items-grid_itemTitleText_5a0255a1'}).text
        if '1ml' in title:
            data_ancientCBD['capacity'] = '1ml'
        elif '0.5ml' in title:
            data_ancientCBD['capacity'] = '0.5ml'
        else:
            data_ancientCBD['capacity'] = '不明'

        stock = item.find('p', {'class': 'items-grid_soldOut_5a0255a1'}) == None
        data_ancientCBD['stock'] = '在庫あり' if stock == True else 'SOLD OUT'
        
        if data_ancientCBD['capacity'] == '1ml':
            data_ancientCBD['0.1mlあたりの値段'] = price / 10
        elif data_ancientCBD['capacity'] == '0.5ml':
            data_ancientCBD['0.1mlあたりの値段'] = price / 5
        else:
            data_ancientCBD['0.1mlあたりの値段'] = 0
        
        data_ancientCBD['URL'] = item.find('a')['href']
        data_ec.append(data_ancientCBD)

def get_data_jomon():
    url = 'https://www.jomon.work/'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    items = soup.find_all('li', {'class': 'items-grid_itemListLI_5a0255a1'})

    for item in items:
        data_jomon = {}
        title = item.find('p', {'class': 'items-grid_itemTitleText_5a0255a1'}).text
        data_jomon['title'] = title
        price = item.find('p', {'class': 'items-grid_price_5a0255a1'}).text
        price = price.replace('¥', '').replace(',', '')
        price = int(price)
        data_jomon['price'] = price
        if '1ml' in title:
            data_jomon['capacity'] = '1ml'
        elif '0.5ml' in title:
            data_jomon['capacity'] = '0.5ml'
        else:
            data_jomon['capacity'] = '不明'
        stock = item.find('p', {'class': 'items-grid_soldOut_5a0255a1'}) == None
        data_jomon['stock'] = '在庫あり' if stock == True else 'SOLD OUT'

        if data_jomon['capacity'] == '1ml':
            data_jomon['0.1mlあたりの値段'] = price / 10
        elif data_jomon['capacity'] == '0.5ml':
            data_jomon['0.1mlあたりの値段'] = price / 5
        else:
            data_jomon['0.1mlあたりの値段'] = 0
        data_jomon['URL'] = item.find('a')['href']   
        data_ec.append(data_jomon)
        
def get_data_aochill():
    url = 'https://aochill.base.shop/'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    items = soup.find_all('li', {'class': 'items-grid_itemListLI_5a0255a1'})
    for item in items:
        data_aochill = {}
        title = item.find('p', {'class': 'items-grid_itemTitleText_5a0255a1'}).text
        data_aochill['title'] = title
        price = item.find('p', {'class': 'items-grid_price_5a0255a1'}).text
        price = price.replace('¥', '').replace(',', '')
        price = int(price)
        data_aochill['price'] = price
        if '1ml' in title:
            data_aochill['capacity'] = '1ml'
        elif '0.5ml' in title:
            data_aochill['capacity'] = '0.5ml'
        else:
            data_aochill['capacity'] = '不明'
        stock = item.find('p', {'class': 'items-grid_soldOut_5a0255a1'}) == None
        data_aochill['stock'] = '在庫あり' if stock == True else 'SOLD OUT'

        if data_aochill['capacity'] == '1ml':
            data_aochill['0.1mlあたりの値段'] = price / 10
        elif data_aochill['capacity'] == '0.5ml':
            data_aochill['0.1mlあたりの値段'] = price / 5
        else:
            data_aochill['0.1mlあたりの値段'] = 0
        data_aochill['URL'] = item.find('a')['href']
        data_ec.append(data_aochill)      
        
def get_data_gray():
    url = 'https://www.graycannabis.jp/categories/3788391'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    items = soup.find_all('div', {'class': 'bs_itemResult__part'})

    for item in items:
        data_gray = {}
        title = item.find('div', {'class': 'bs_itemCard__title'}).text
        data_gray['title'] = title
        price = item.find('div', {'class': 'bs_itemCard__price'}).text
        price = price.replace('¥', '').replace(',', '')
        price = int(price)
        data_gray['price'] = price


        if '1mL' in title:
            data_gray['capacity'] = '1ml'
        elif '0.5mL' in title:
            data_gray['capacity'] = '0.5ml'
        else:
            data_gray['capacity'] = '不明'
        stock = item.find('span', {'class': 'bs_itemCard__soldout'}) == None
        data_gray['stock'] = '在庫あり' if stock == True else 'SOLD OUT'

        if data_gray['capacity'] == '1ml':
            data_gray['0.1mlあたりの値段'] = price / 10
        elif data_gray['capacity'] == '0.5ml':
            data_gray['0.1mlあたりの値段'] = price / 5
        else:
            data_gray['0.1mlあたりの値段'] = 0
        data_gray['URL'] = item.find('a')['href']
        data_ec.append(data_gray)

def get_df_ec():
    get_data_SLC()
    get_data_city420()
    get_data_macaroniCBD()
    get_data_madoromi()
    get_data_ancient()
    get_data_jomon()
    get_data_aochill()
    get_data_gray()
    df_ec = pd.DataFrame(data_ec)
    return df_ec

st.title('CBDリキッド比較')

latest_iteration = st.empty()
bar = st.progress(0)
    
for i in range(100):
    latest_iteration.text(f'進行状況 {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)  

df_ec = get_df_ec()  




    
    
liquid = st.radio(
     "欲しいリキッドは何ですか？",
     ('すべて', 'HHC', 'CBN', 'CBG', 'CBD'))


     

if liquid == 'すべて':
    df_ec
elif liquid == 'HHC':
    df_ec[df_ec['title'].str.contains('HHC')]
elif liquid == 'CBN':
    df_ec[df_ec['title'].str.contains('CBN')]
elif liquid == 'CBG':
    df_ec[df_ec['title'].str.contains('CBG')]
elif liquid == 'CBD':
    df_ec[df_ec['title'].str.contains('CBD')]
else:
    df_ec
        



# st.write('CBDリキッド在庫情報', df_ec)


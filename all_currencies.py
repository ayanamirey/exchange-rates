import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'}

# DOLLAR
DOLLAR_SUM = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%81%D1%83%D0%BC%D1%83&hl=ru&sxsrf=APq-WBt6U16qzIHJ0xxTRWW3OKUfR_jztw%3A1648039856730&source=hp&ei=sBc7YrGdJcqHxc8PuJqqiAw&iflsig=AHkkrS4AAAAAYjslwJ4Evq4Emq5vpT_dUwR7UQfA_DYa&ved=0ahUKEwixterxotz2AhXKQ_EDHTiNCsEQ4dUDCAc&uact=5&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%81%D1%83%D0%BC%D1%83&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEMQCMgUIABCABDIFCAAQgAQyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeOgcIIxDqAhAnOgcILhDqAhAnOgQIIxAnOhAIABCABBCHAhCxAxCDARAUOgsIABCABBCxAxCDAToICAAQsQMQgwE6CggAELEDEIMBEEM6BAgAEEM6DggAEIAEELEDEIMBEMkDOgkIIxAnEEYQggI6CAgAEIAEELEDOgsIABCABBCxAxDJAzoKCAAQgAQQhwIQFDoHCAAQgAQQClCWAViiEWD6FWgAcAB4AIABuQKIAaITkgEIMC4xMC4zLjGYAQCgAQGwAQo&sclient=gws-wiz'
full_page = requests.get(DOLLAR_SUM, headers=headers)
soup = BeautifulSoup(full_page.content, 'html.parser')

convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
dollartosum = convert[0].text.replace(',', '.').split()
dollartosum = float("".join(dollartosum))

# RUBLE
DOLLAR_RUBLE = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&hl=ru&sxsrf=APq-WBuV8pYQUgoVw0fbBrPOa9dSQ5CugA%3A1648042622213&source=hp&ei=fiI7Yt70Cd2Cxc8P5ZCkyAE&iflsig=AHkkrS4AAAAAYjswjkcogVWHHq_p3pFmF8jTH7aiNZ80&oq=ljkkfh&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCCMQsQIQJzIHCCMQsQIQJzIHCCMQsQIQJzIKCAAQsQMQgwEQCjINCAAQsQMQgwEQyQMQCjIKCAAQsQMQgwEQCjIKCAAQsQMQgwEQCjIKCAAQsQMQgwEQCjIKCAAQsQMQgwEQCjIKCAAQsQMQgwEQCjoECCMQJzoICAAQgAQQsQM6CAguEIAEELEDOgUIABCABDoLCC4QgAQQxwEQ0QM6CggAEAoQARBDECo6BAguEEM6BQguEIAEOgQIABAKOgkIABCABBAKEAE6CwgAEIAEEAoQARAqOggILhAKEAEQQzoQCAAQgAQQChABECoQRhCCAlAvWLwEYP8RaABwAHgAgAHPAogB6QuSAQcwLjEuNC4xmAEAoAEBsAEA&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'}
full_page = requests.get(DOLLAR_RUBLE, headers=headers)

soup = BeautifulSoup(full_page.content, 'html.parser')
convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
dollartoruble = convert[0].text.replace(',', '.').split()
dollartoruble = float("".join(dollartoruble))

# HRYVNIA
DOLLAR_HRYVNIA = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D0%B5&hl=ru&sxsrf=APq-WBttXHCCMOpIGHStR9i7E7QdRMcZ2w%3A1648042901687&source=hp&ei=lSM7YuOhJdCSxc8P_eiqyAQ&iflsig=AHkkrS4AAAAAYjsxpXY6-8Tqh_iBfukttpmmM5C5nHQu&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D0%B3%D1%80%D0%B8&gs_lcp=Cgdnd3Mtd2l6EAMYADIKCAAQgAQQRhCCAjIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMggIABCABBDJAzoHCCMQ6gIQJzoECCMQJzoQCAAQgAQQhwIQsQMQgwEQFDoLCAAQgAQQsQMQgwE6CAgAELEDEIMBOgkIIxAnEEYQggI6CggAELEDEIMBEEM6BAgAEEM6DggAEIAEELEDEIMBEMkDOgoIABCABBCHAhAUUPAEWL4cYIkxaAFwAHgAgAGtAYgB_QqSAQQwLjEymAEAoAEBsAEK&sclient=gws-wiz'
full_page = requests.get(DOLLAR_HRYVNIA, headers=headers)

soup = BeautifulSoup(full_page.content, 'html.parser')
convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
dollartohryvnia = convert[0].text.replace(',', '.').split()
dollartohryvnia = float("".join(dollartohryvnia))

# YUAN
DOLLAR_YUAN = 'https://www.google.com/search?q=1+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%B2+%D1%8E%D0%B0%D0%BD%D1%8F%D1%85&hl=ru&sxsrf=APq-WBsm7W9DyEVLjD5dgJ2J9eLvJTshfg%3A1648049843269&source=hp&ei=sz47YsHHDdaGxc8PxeqL0Ak&iflsig=AHkkrS4AAAAAYjtMw3dPcEAaOjJMXohDa2RUCKvjIeC5&oq=1+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%B2+%D1%8E%D0%B0%D0%BD%D1%8F&gs_lcp=Cgdnd3Mtd2l6EAMYADIKCAAQgAQQRhCCAjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeOgcIIxDqAhAnOgQIIxAnOgQIABBDOgUIABCABDoKCAAQsQMQgwEQQzoHCAAQyQMQQzoKCAAQgAQQhwIQFDoJCAAQQxBGEIICOgkIABAKEEYQggI6BAgAEAo6BwgAEMkDEAo6CQgAEMkDEBYQHjoGCAAQDRAeOgUIIRCgAToICAAQFhAKEB46CAghEBYQHRAeOggIABANEAUQHjoHCCEQChCgAVDdAljzmgFg4r0BaAxwAHgAgAHZAogBmh2SAQgwLjI0LjEuMZgBAKABAbABCg&sclient=gws-wiz'
full_page = requests.get(DOLLAR_YUAN, headers=headers)

soup = BeautifulSoup(full_page.content, 'html.parser')
convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
dollartoyuan = convert[0].text.replace(',', '.').split()
dollartoyuan = float("".join(dollartoyuan))

# WON
DOLLAR_WON = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D0%B2%D0%BE%D0%BD%D1%83&hl=ru&sxsrf=APq-WBvh7yV1uXM-zoL9wYOiJ-b_ugpM_w%3A1648045251822&source=hp&ei=wyw7YuzrLqSFxc8PsrmKaA&iflsig=AHkkrS4AAAAAYjs60zZDrVU_2hHCz6D9BAvTFi8YjWZ0&ved=0ahUKEwis2bj-ttz2AhWkQvEDHbKcAg0Q4dUDCAc&uact=5&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D0%B2%D0%BE%D0%BD%D1%83&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEMQCEEYQggIyBQgAEIAEMgUIABCABDIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjoHCCMQyQMQJzoLCAAQgAQQsQMQgwE6CggAEIAEEIcCEBQ6BwgAEIAEEAo6CAgAEBYQChAeUABY2A1gwRVoAXAAeAGAAckBiAH5BpIBBTAuNS4xmAEAoAECoAEB&sclient=gws-wiz'
full_page = requests.get(DOLLAR_WON, headers=headers)

soup = BeautifulSoup(full_page.content, 'html.parser')
convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
dollartowon = convert[0].text.replace(',', '.').split()
dollartowon = float("".join(dollartowon))

# TENGE
DOLLAR_TENGE = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%82%D0%B5%D0%BD%D0%B3%D0%B5&hl=ru&sxsrf=APq-WBsM-7F-bpbw9XxfuWRWaHLjbLF9Vg%3A1648045606413&source=hp&ei=Ji47YqTlFcCPxc8PjdKPoAE&iflsig=AHkkrS4AAAAAYjs8NqA8LCNOPxEQjWZ-_V2kbi-YjVDY&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+&gs_lcp=Cgdnd3Mtd2l6EAMYAzIJCCMQJxBGEIICMgQIIxAnMgQIIxAnMgoIABCxAxCDARBDMgoIABCxAxCDARBDMgQIABBDMgQIABBDMg4IABCABBCxAxCDARDJAzIICAAQgAQQsQMyBQgAEIAEOgcIIxDqAhAnOhAIABCABBCHAhCxAxCDARAUOgsIABCABBCxAxCDAToICAAQsQMQgwFQ4gNYxQ5grCVoAHAAeACAAcgCiAG-DZIBBzAuNy4yLjGYAQCgAQGwAQo&sclient=gws-wiz'
full_page = requests.get(DOLLAR_TENGE, headers=headers)

soup = BeautifulSoup(full_page.content, 'html.parser')
convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
dollartotenge = convert[0].text.replace(',', '.').split()
dollartotenge = float("".join(dollartotenge))

# SUM TO DOLLAR
SUM_DOLLAR = 'https://www.google.com/search?q=%D1%81%D1%83%D0%BC+%D0%B2+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80&hl=ru&sxsrf=APq-WBteBf7No3AVWakQEg10ixLiXQtGRw%3A1648046581126&source=hp&ei=9TE7YpvmA9SIxc8PzdOMMA&iflsig=AHkkrS4AAAAAYjtABVEjISHlVoX1FwAvlRiqtWNEn7nP&oq=%D1%81%D1%83%D0%BC+&gs_lcp=Cgdnd3Mtd2l6EAMYADIECCMQJzIKCAAQsQMQgwEQQzILCAAQgAQQsQMQgwEyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBQgAEIAEMgcIABDJAxBDMgUIABCABDoHCCMQ6gIQJzoICAAQgAQQsQM6BwgAELEDEENQrgVYzQdg4hFoAHAAeACAAa0CiAG7CZIBBzAuMS4zLjGYAQCgAQGwAQo&sclient=gws-wiz'
full_page = requests.get(SUM_DOLLAR, headers=headers)

soup = BeautifulSoup(full_page.content, 'html.parser')
convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 6})
sumtodollar = convert[0].text.replace(',', '.').split()
sumtodollar = float("".join(sumtodollar))

# HRYVNIA TO DOLLAR
HRYVNIA_DOLLAR = 'https://www.google.com/search?q=%D0%B3%D1%80%D0%B8%D0%B2%D0%B5%D0%BD+%D0%B2+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0%D1%85&hl=ru&sxsrf=APq-WBua2VgvYA4-z4sDLKiDsArjuvuhAw%3A1648049380778&source=hp&ei=5Dw7YrSDLYKExc8P0buwyAM&iflsig=AHkkrS4AAAAAYjtK9DcCnsMPERiuj-P24TEtPBqHEutx&oq=%D0%B3%D1%80%D0%B8%D0%B2&gs_lcp=Cgdnd3Mtd2l6EAMYAzIECCMQJzIKCAAQgAQQhwIQFDIKCAAQgAQQhwIQFDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQguEIAEMgUIABCABDIICC4QgAQQ1AI6BwgjEOoCECc6BAguECc6CwgAEIAEELEDEIMBOggIABCABBCxAzoRCC4QgAQQsQMQgwEQxwEQ0QM6CAguELEDEIMBOggILhCABBCxAzoLCC4QgAQQsQMQgwE6BAgAEAo6BwguEIAEEAo6CwguEIAEELEDENQCUKMLWPIpYNZYaAJwAHgBgAGrAogBgQeSAQUwLjUuMZgBAKABAbABCg&sclient=gws-wiz'
full_page = requests.get(HRYVNIA_DOLLAR, headers=headers)

soup = BeautifulSoup(full_page.content, 'html.parser')
convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 3})
hryvniatodollar = convert[0].text.replace(',', '.').split()
hryvniatodollar = float("".join(hryvniatodollar))

# RUBLE TO DOLLAR
RUBLE_DOLLAR = 'https://www.google.com/search?q=%D1%80%D1%83%D0%B1%D0%BB%D1%8C+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1%83&hl=ru&sxsrf=APq-WBuWtHp7i_MFhvKre8PcalqrZ_lcbg%3A1648050083792&source=hp&ei=oz87Yva3Lf2Qxc8P97qzcA&iflsig=AHkkrS4AAAAAYjtNs9EKUXRyDQfNhsmnorOeVTQZ376l&oq=%D1%80%D0%BA%D0%B1%D0%BB%D1%8C+%D0%BA+&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCAAQsQMQCjIKCAAQsQMQgwEQCjIHCAAQyQMQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjoHCCMQ6gIQJzoLCC4QgAQQxwEQrwE6BQgAEIAEOgkILhCABBAKEAE6CAgAELEDEIMBOgQIABABOg8IABCxAxCDARAKEEYQggJQwgFYrRlgjyZoAXAAeAGAAb4FiAGJF5IBDTAuNC4xLjMuMS4wLjGYAQCgAQGwAQo&sclient=gws-wiz'
full_page = requests.get(RUBLE_DOLLAR, headers=headers)

soup = BeautifulSoup(full_page.content, 'html.parser')
convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 3})
rubletodollar = convert[0].text.replace(',', '.').split()
rubletodollar = float("".join(rubletodollar))

# TENGE TO DOLLAR
TENGE_DOLLAR = 'https://www.google.com/search?q=%D1%82%D0%B5%D0%BD%D0%B3%D0%B5+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1%83&hl=ru&sxsrf=APq-WBv_ejKAfASiGVZnKcBpcaEFbkD8YA%3A1648050635914&source=hp&ei=y0E7YrLANJuOxc8P3IaZ6AM&iflsig=AHkkrS4AAAAAYjtP2wnwATRfpMwM1hZ1zhuF8hWyJLZ3&oq=%D1%82%D0%B5%D0%BD%D0%B3%D0%B5+&gs_lcp=Cgdnd3Mtd2l6EAMYADIMCAAQsQMQQxBGEIICMgQIABBDMhAIABCABBCHAhCxAxCDARAUMgoIABCxAxCDARBDMg4ILhCABBCxAxDHARCvATIECAAQQzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgjEOoCECc6BAgjECc6CAgAEIAEELEDOg4ILhCABBCxAxCDARDUAjoLCAAQgAQQsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggIABCxAxCDAToLCC4QgAQQxwEQrwE6CwguEIAEEMcBENEDOg8ILhCABBDHARCvARAKEAE6CQgAEIAEEAoQAToRCC4QgAQQxwEQrwEQChABECo6BwgAEIAEEAo6CggAEIAEEIcCEBQ6BwgAELEDEEM6CwguEIAEELEDEIMBOg0IABCABBCHAhCxAxAUUJINWLwwYLY5aAJwAHgAgAH3AYgB6QySAQUwLjkuMpgBAKABAbABCg&sclient=gws-wiz'
full_page = requests.get(TENGE_DOLLAR, headers=headers)

soup = BeautifulSoup(full_page.content, 'html.parser')
convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 4})
tengetodollar = convert[0].text.replace(',', '.').split()
tengetodollar = float("".join(tengetodollar))

# YUAN TO DOLLAR
YUAN_DOLLAR = 'https://www.google.com/search?q=%D1%8E%D0%B0%D0%BD%D1%8C+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1%83&hl=ru&sxsrf=APq-WBvfat02WRmg_3E1USchZsnuFm22rg%3A1648051080116&source=hp&ei=iEM7YtybA5WFxc8P_96SoAM&iflsig=AHkkrS4AAAAAYjtRmMbMZQbpS1dtlrBIP3_cV-NZNJd5&oq=%D1%8E%D0%B0%D0%BD%D1%8C&gs_lcp=Cgdnd3Mtd2l6EAMYADIPCAAQsQMQgwEQQxBGEIICMgQIABBDMgQIABBDMgoIABCxAxCDARBDMgoIABCxAxCDARBDMgUIABCABDIECAAQQzIFCC4QgAQyBQgAEIAEMgUIABCABDoHCCMQ6gIQJzoECCMQJzoRCC4QgAQQsQMQgwEQxwEQ0QM6EAgAEIAEEIcCELEDEIMBEBQ6CAguEIAEELEDOggIABCABBCxAzoLCAAQgAQQsQMQgwE6CggAEIAEEIcCEBRQkxhY3B1goyloAXAAeACAAfkBiAH6BZIBBTAuNC4xmAEAoAEBsAEK&sclient=gws-wiz'
full_page = requests.get(YUAN_DOLLAR, headers=headers)

soup = BeautifulSoup(full_page.content, 'html.parser')
convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
yuantodollar = convert[0].text.replace(',', '.').split()
yuantodollar = float("".join(yuantodollar))

# WON TO DOLLAR
WON_DOLLAR = 'https://www.google.com/search?q=%D0%B2%D0%BE%D0%BD+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1%83&hl=ru&sxsrf=APq-WBsb_ML71_iscJTgXjVyE49r-nrz4Q%3A1648051573279&source=hp&ei=dUU7YvnjDaaLxc8Pl6WB4A8&iflsig=AHkkrS4AAAAAYjtThXU5npibJNoZCq82ePQ4W12iPDXk&oq=%D0%B2%D0%BE%D0%BD+%D0%BA+&gs_lcp=Cgdnd3Mtd2l6EAMYADIJCAAQQxBGEIICMgQIABBDMgUIABCABDIECAAQQzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoHCCMQ6gIQJzoECCMQJzoKCAAQgAQQhwIQFDoICAAQsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggILhCABBCxAzoLCAAQgAQQsQMQgwE6CgguEMcBENEDEEM6CAguEIAEENQCOgUILhCABDoHCC4QgAQQClChCFi_DWCnFWgAcAB4AIABkgGIAfwGkgEDMC43mAEAoAEBsAEK&sclient=gws-wiz'
full_page = requests.get(WON_DOLLAR, headers=headers)

soup = BeautifulSoup(full_page.content, 'html.parser')
convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 5})
wontodollar = convert[0].text.replace(',', '.').split()
wontodollar = float("".join(wontodollar))
from bs4 import BeautifulSoup


def parser_run(html_doc):
    zbxm_list = []  # 招标项目列表
    soup = BeautifulSoup(html_doc, 'html.parser')
    for tr in soup.find_all('tr', class_='hover_tr'):
        time = tr.find('td', class_='color_9').get_text()
        td = tr.find('td', class_='zblist_xm')
        title = td.get_text()
        link = td.a['href']
        # print(title, link, time)
        zbxm = {'title': title, 'link': link, 'time': time}
        zbxm_list.append(zbxm)
    # print(zbxm_list)
    return zbxm_list

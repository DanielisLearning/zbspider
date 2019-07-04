from bs4 import BeautifulSoup
import jieba

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

def is_kw_title(title, kw_list):
    """
    解析结果中title部分
    是否包含一些关键词
    bool 函数
    @param title : 招标文件的标题，字符串
    @param *args : 关键词列表
    @return : True or False
    """
    seg_list = jieba.cut(title)
    kw_title = [x for x in seg_list if x in kw_list]
    if kw_title is None:
        return False
    else:
        return True

import requests
import time
from bs4 import BeautifulSoup as BS


def f():
    global cur1
    cur1 = ""
    hits = requests.get("https://abiturient.tsu.ru/rating?fp=1&p=09.03.04_%D0%9E_%D0%91_%D0%9E%D0%9F_00000373&l=1&f=22&d=09.03.04&b=%D0%91%D1%8E%D0%B4%D0%B6%D0%B5%D1%82&ef=1")
    html_hits = BS(hits.content, 'html.parser')


    table_hits = html_hits.find("div", class_= "content-table").find("table").find_all("tr")
    abiturients_hits = []


    for tr in table_hits[4:]:
        line = tr.find_all("td")
        information = []
        for el in line:
            information.append(el.text.replace("\n", ""))
        abiturients_hits.append([s.strip() for s in [information[0], information[1],information[2], information[3], information[5], information[-2]]])
        if information[2].strip() == "166-791-589 28":
            cur1 = information[0].strip()
    #abiturients_hits = abiturients_hits[4:]
    # for el in abiturients_hits:
    #     print(el)
    return abiturients_hits
#print(f())
m_stariy = f()
kolvo_staroe = len(m_stariy)
kolvo_novoe = len(m_stariy)
your_position = cur1
while True:
    #m_stariy = f()
    #time.sleep(10)
    time.sleep(0.09)
    m_noviy = f()
    if m_noviy != m_stariy:
        kolvo_novoe = len(m_noviy)
        # for el1 in m_noviy:
        #     if el1 not in m_stariy:
        #         print(f"Появился новый абитуриент:\nПозиция в рейтинге: {el1[0]}\nСНИЛС: {el1[2]}\nДокумент: {el1[3]}\nСогласие: {el1[4]}\nСумма баллов: {el1[5]}")
        #         print("\n \n \n")
        #     if el1[2] == "166-791-589 28":
        #         your_position = el1[0]
        for i in range(len(m_noviy)):
            flag = False
            for el in m_stariy:
                if m_noviy[i][1] == el[1]:
                    flag = True
                    if m_noviy[i][0] != el[0]:
                        print(f"Абитуриент поменял позицию:\nСтарая позиция: {el[0]}\nНовая позиция: {m_noviy[i][0]}\nСНИЛС: {m_noviy[i][2]}\nДокумент: {m_noviy[i][3]}\nСогласие: {m_noviy[i][4]}\nСумма баллов: {m_noviy[i][5]}")
                        print("\n \n \n")
            if not (flag):
                print(f"Появился новый абитуриент:\nПозиция в рейтинге: {m_noviy[i][0]}\nСНИЛС: {m_noviy[i][2]}\nДокумент: {m_noviy[i][3]}\nСогласие: {m_noviy[i][4]}\nСумма баллов: {m_noviy[i][5]}")
                print("\n \n \n")
            if m_noviy[i][2] == "166-791-589 28":
                your_position = m_noviy[i][0]
    else:
        print('Обновлений нет')
    print('=' * 20)
    print('=' * 20)
    print(f"На текущий момент вы на {your_position} месте\nБыло абитуриентов: {kolvo_staroe}\nСтало абитуриентов: {kolvo_novoe}")
    kolvo_staroe = kolvo_novoe
    print('=' * 20)
    print('=' * 20)
    m_stariy = m_noviy[:]


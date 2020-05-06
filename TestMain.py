import re
import threadpool
from bs4 import BeautifulSoup
from lib.item.ershou import *
from lib.zone.city import get_city
from lib.spider.base_spider import *
from lib.utility.date import *
from lib.utility.path import *
from lib.zone.area import *

if __name__ == "__main__":
    doc = '<div class="info clear"><div class="title"><a class="" href="https://gz.lianjia.com/ershoufang/108401162034.html" target="_blank" data-log_index="1" data-el="ershoufang" data-housecode="108401162034" data-is_focus="" data-sl="">龙口东路 南向两房 新装修保养好</a><!-- 拆分标签 只留一个优先级最高的标签--><span class="new tagBlock">新上</span></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span><a href="https://gz.lianjia.com/xiaoqu/2111103317829/" target="_blank" data-log_index="1" data-el="region">龙口东路翠竹苑 </a>   -  <a href="https://gz.lianjia.com/ershoufang/longkoudong/" target="_blank">龙口东</a> </div></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span>2室1厅 | 77.99平米 | 南 | 其他 | 中楼层(共7层) | 1995年建 | 塔楼</div></div><div class="followInfo"><span class="starIcon"></span>2人关注 / 4天以前发布</div><div class="tag"><span class="subway">近地铁</span><span class="vr">VR房源</span><span class="five">房本满两年</span></div><div class="priceInfo"><div class="totalPrice"><span>380</span>万</div><div class="unitPrice" data-hid="108401162034" data-rid="2111103317829" data-price="48725"><span>单价48725元/平米</span></div></div></div>'
    soup = BeautifulSoup(doc, "lxml")
    id = soup.find('div', class_='title').find(name='a').get('href')
    print(id)
    id = id[id.rfind('/') + 1 : id.rfind('.')]
    print(id)

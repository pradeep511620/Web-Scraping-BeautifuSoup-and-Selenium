import requests
from bs4 import BeautifulSoup
from typing import TextIO
import re

myresult=['https://dodge.ptplace.com/productDetail/_pn=140031?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140032?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140035?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140036?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140038?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140039?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140042?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140044?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140046?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140049?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140051?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140056?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140058?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140059?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140064?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140066?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140067?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140069?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140070?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140071?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140072?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140074?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140075?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140076?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140077?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140079?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140082?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140083?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140084?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140085?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140086?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140087?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140088?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140089?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140090?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140094?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140097?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140098?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140100?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140101?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140102?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140103?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140105?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140106?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140108?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140109?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140110?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140115?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140117?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140118?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140120?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140121?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140125?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140126?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140132?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140139?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140140?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140142?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140146?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140147?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140149?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140150?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140151?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140152?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140153?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140154?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140155?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140156?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140159?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140160?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140161?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140162?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140167?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140168?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140172?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140174?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140176?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140178?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140180?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140183?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140184?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140185?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140186?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140189?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140190?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140191?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140193?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140194?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140195?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140199?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140200?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140201?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140212?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140214?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140215?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140218?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140220?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140221?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140222?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140223?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140224?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140225?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140231?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140232?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140233?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140237?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140238?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140240?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140242?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140244?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140245?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140247?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140249?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140256?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140262?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140264?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140266?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140268?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140269?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140273?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140274?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140275?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140285?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140287?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140288?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140290?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140292?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140295?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140296?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140297?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140302?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140303?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140304?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140305?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140306?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140307?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140309?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140310?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140316?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140317?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140319?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140320?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140321?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140322?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140323?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140324?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140331?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140333?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140334?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140337?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140338?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140339?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140340?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140341?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140344?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140345?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140346?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140347?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140348?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140350?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140351?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140354?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140355?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140356?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140357?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140358?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140383?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140384?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140385?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140386?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140389?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140390?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140392?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140393?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140395?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140398?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140400?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140408?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140409?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140411?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140412?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140420?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140421?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140429?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140431?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140432?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140434?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140435?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140437?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140439?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140441?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140442?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140443?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140456?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140457?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140459?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140463?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140464?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140465?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140469?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140471?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140473?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140475?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140477?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140479?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140480?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140481?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140493?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140494?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140495?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140502?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140504?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140507?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140508?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140509?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140512?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140514?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140515?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140517?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140518?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140521?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140522?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140523?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140526?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140527?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140532?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140533?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140534?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140536?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140538?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140539?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140549?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140550?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140555?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140557?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140558?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140565?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140566?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140567?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140568?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140570?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140574?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140576?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140578?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140582?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140583?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140584?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140585?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140586?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140591?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140593?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140594?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140595?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140596?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140597?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140598?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140599?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140600?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140601?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140602?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140603?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140604?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140605?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140615?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140620?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140621?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140622?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140627?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140630?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140631?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140632?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140633?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140635?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140636?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140638?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140641?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140642?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140643?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140644?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140647?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140648?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140650?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140654?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140655?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140658?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140661?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140666?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140669?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140671?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140672?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140673?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140682?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140683?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140689?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140690?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140691?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140692?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140693?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140694?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140695?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140696?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140701?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140702?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140705?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140707?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140708?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140710?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140712?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140713?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140714?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140717?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140718?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140719?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140721?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140724?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140725?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140728?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140738?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140739?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140740?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140743?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140744?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140747?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140748?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140751?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140752?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140758?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140763?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140765?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140766?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140767?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140768?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140769?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140771?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140772?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140773?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140774?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140777?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140779?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140783?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140785?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140790?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140791?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140794?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140795?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140797?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140798?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140801?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140804?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140807?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140810?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140811?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140812?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140813?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140817?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140819?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140820?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140825?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140827?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140828?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140830?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140832?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140834?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140836?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140837?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140839?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140840?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140842?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140843?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140844?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140845?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140848?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140849?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140851?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140853?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140854?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140856?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140857?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140858?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140859?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140861?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140862?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140863?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140864?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140866?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140867?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140868?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140869?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140872?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140874?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140876?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140883?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140886?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140887?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140888?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140889?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140891?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140897?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140898?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140903?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140904?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140906?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140907?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140908?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140910?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140911?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140912?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140914?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140915?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140916?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140918?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140920?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140922?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140925?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140926?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140929?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140930?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140932?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140936?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140942?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140945?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140947?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140948?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140949?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140951?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140952?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140954?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140957?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140958?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140961?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140962?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140963?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140967?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140969?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140974?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140975?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140977?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140978?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140979?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140982?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140985?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140986?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140996?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=140997?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=141010?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=141011?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=141014?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=141015?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=141020?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=141022?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=141025?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=141027?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=141028?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=141031?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=141033?reference=PartSearchListLink',
'https://dodge.ptplace.com/productDetail/_pn=141048?reference=PartSearchListLink']

for row in myresult:

 try:

    product_url = row

    #page = requests.get(product_url)

    headers = {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)", "Referer": "http://example.com"}

    result = requests.get(product_url, headers=headers)

    if result.status_code == 200:

        print("site woking")

    else:

        print("site not working"+str(result.status_code))

    #a = (result.content.decode())


    soup = BeautifulSoup(result.content,'html.parser')

    #print(soup.prettify())





    bread = soup.find("ol",class_="breadcrumb pb-0 mb-0 px-0 pt-3 pt-md-0").find_all("li")
    list1 = []
    for b in bread:
        list1.append(b.text.strip())
    print(list1)





    # qnt = (soup.prettify().replace('data-ship-pack-quantity="', "raptor:").split("raptor:")[1].split('"')[0])

    #weight = soup.find("div",class_="rta sidebar__shipping-pane")



    #detail = soup.find("div",class_="copyTextSection textSection")
    #image enhanced-content__carousel-main-image image--loaded
    #soup.find("span",attrs={'data-automated-test':'leaf'})


    c = (product_url)
    print(c)



    # zxqw = qnt
    #https://static.grainger.com/rp/s/is/image/Grainger/29DJ11_GC01?hei=804&wid=804
    try:


     prod = soup.find_all("bdo",class_="data-label text-uppercase text-transparent-dark")


     specs = soup.find_all("td",class_="w-50 bg-white css-k6e94w ewehtpn0")



     i = 0
    except:
        pass
    if(len(prod)>0):

     while i < len(prod):


        j = 0

        while j < len(specs):

            z = (prod[i].text if prod else "not given")
            print(z)

            i += 1

            x = (specs[j].text if specs else "not given")
            print(x)

            j += 1
            save_details: TextIO = open("dodge-3333.txt", "a+", encoding="utf-8")
            save_details.write("\n"+c+"\t"+" / ".join(list1)+"\t"+"RP_"+z+"\t"+"RP_"+x)
            save_details.close()
            print("\n**Record stored into txt file.**")
    else:
        save_details: TextIO = open("dodge-3333.txt", "a+", encoding="utf-8")
        save_details.write("\n" + c + "\t" + " / ".join(list1))
        save_details.close()
        print("\n**Record stored into txt file.**")





 except AttributeError:

   pass

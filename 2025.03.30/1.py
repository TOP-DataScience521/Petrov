high_domains = ['ac', 'ad', 'ae', 'af', 'ag', 'ai', 'al', 'am', 'an', 'ao', 'aq', 'ar', 'as', 'at', 'au', 'aw', 'ax', 'az', 'ba', 'bb', 'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bl', 'bm', 'bn', 'bo', 'bq', 'br', 'bs', 'bt', 'bv', 'bw', 'by', 'bz', 'ca', 'cc', 'cd', 'cf', 'cg', 'ch', 'ci', 'ck', 'cl', 'cm', 'cn', 'co', 'cr', 'cu', 'cv', 'cw', 'cx', 'cy', 'cz', 'de', 'dj', 'dk', 'dm', 'do', 'dz', 'ec', 'ee', 'eg', 'eh', 'er', 'es', 'et', 'eu', 'fi', 'fj', 'fk', 'fm', 'fo', 'fr', 'ga', 'gb', 'gd', 'ge', 'gf', 'gg', 'gh', 'gi', 'gl', 'gm', 'gn', 'gp', 'gq', 'gr', 'gs', 'gt', 'gu', 'gw', 'gy', 'hk', 'hm', 'hn', 'hr', 'ht', 'hu', 'id', 'ie', 'il', 'im', 'in', 'io', 'iq', 'ir', 'is', 'it', 'je', 'jm', 'jo', 'jp', 'ke', 'kg', 'kh', 'ki', 'km', 'kn', 'kp', 'kr', 'kw', 'ky', 'kz', 'la', 'lb', 'lc', 'li', 'lk', 'lr', 'ls', 'lt', 'lu', 'lv', 'ly', 'ma', 'mc', 'md', 'me', 'mf', 'mg', 'mh', 'mk', 'ml', 'mm', 'mn', 'mo', 'mp', 'mq', 'mr', 'ms', 'mt', 'mu', 'mv', 'mw', 'mx', 'my', 'mz', 'na', 'nc', 'ne', 'nf', 'ng', 'ni', 'nl', 'no', 'np', 'nr', 'nu', 'nz', 'om', 'pa', 'pe', 'pf', 'pg', 'ph', 'pk', 'pl', 'pm', 'pn', 'pr', 'ps', 'pt', 'pw', 'py', 'qa', 're', 'ro', 'rs', 'ru', 'rw', 'sa', 'sb', 'sc', 'sd', 'se', 'sg', 'sh', 'si', 'sj', 'sk', 'sl', 'sm', 'sn', 'so', 'sr', 'ss', 'st', 'su', 'sv', 'sx', 'sy', 'sz', 'tc', 'td', 'tf', 'tg', 'th', 'tj', 'tk', 'tl', 'tm', 'tn', 'to', 'tp', 'tr', 'tt', 'tv', 'tw', 'tz', 'ua', 'ug', 'uk', 'um', 'us', 'uy', 'uz', 'va', 'vc', 've', 'vg', 'vi', 'vn', 'vu', 'wf', 'ws', 'ಭಾರತ', '한국', 'ଭାରତ', 'ভাৰত', 'ভারত', 'ישראל', 'বাংলা', 'қаз', 'срб', 'бг', 'бел', 'சிங்கப்பூர்', 'мкд', 'ею', '中国', '中國', 'భారత్', 'ලංකා', 'ભારત', 'भारतम्', 'भारत', 'भारोत', 'укр', '香港', '台湾', '台灣', 'мон', 'الجزائر', 'عمان', 'ایران', 'امارات', 'موريتانيا', 'پاکستان', 'الاردن', 'بارت', 'بھارت', 'المغرب', 'البحرين', 'السعودية', 'ڀارت', 'سودان', 'عراق', 'مليسيا', '澳門', 'გე', 'ไทย', 'سورية', 'рф', 'تونس', 'ລາວ', 'ευ', 'ελ', 'ഭാരതം', 'ਭਾਰਤ', 'مصر', 'قطر', 'இலங்கை', 'இந்தியா', 'հայ', '新加坡', 'فلسطين', 'ye', 'yt', 'za', 'zm', 'zw']

email = input('Введите email: ')

if '.' in email and '@' in email:
    check = email.rsplit(sep='.', maxsplit=1)
    check_1 = str(check[1])
    check_2 = str(''.join(check[0].split(sep='@')))   

    for symbol in check_2:
        if symbol == '_' or symbol == '.' or symbol.isalnum():
            check_2_result = 1
        else:
            check_2_result = 0  

    if high_domains.index(check_1)>=0:
        check_1_result = 1
    else:
        check_1_result = 0        
            
    if check_1_result+check_2_result==2:
        print('да')
    else:
        print('нет')
        
else:
    print('нет')

# Введите email: 137an_d....reyPetrovأ__ندري.بتروف@yan安декс.德烈.ru
# да
# Введите email: abcde@fghij
# нет

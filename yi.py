import tkinter as tk
import random
import time

# 易經六十四卦的名稱對應表（下卦與上卦）
TRIGRAM_NAMES = {
    "111": "乾", "000": "坤", "100": "震", "011": "巽", "010": "坎",
    "001": "艮", "101": "離", "110": "兌"
}

# 卦象編號對應表，代表每個六十四卦的編號
HEXAGRAM_NAMES = {
    "111111": "乾卦",
    "000000": "坤卦",
    "010001": "屯卦",
    "100010": "蒙卦",
    "010111": "需卦",
    "111010": "訟卦",
    "000010": "師卦",
    "010000": "比卦",
    "110111": "小畜卦",
    "111011": "履卦",
    "000111": "泰卦",
    "111000": "否卦",
    "111101": "同人卦",
    "101111": "大有卦",
    "000100": "謙卦",
    "001000": "豫卦",
    "011001": "隨卦",
    "100110": "蠱卦",
    "000011": "臨卦",
    "110000": "觀卦",
    "101001": "噬嗑卦",
    "100101": "賁卦",
    "100000": "剝卦",
    "000001": "復卦",
    "111001": "無妄卦",
    "100111": "大畜卦",
    "100001": "頤卦",
    "011110": "大過卦",
    "010010": "坎卦",
    "101101": "離卦",
    "011100": "咸卦",
    "001110": "恆卦",
    "111100": "遯卦",
    "001111": "大壯卦",
    "101000": "晉卦",
    "000101": "明夷卦",
    "110101": "家人卦",
    "101011": "睽卦",
    "010100": "蹇卦",
    "001010": "解卦",
    "100011": "損卦",
    "110001": "益卦",
    "011111": "夬卦",
    "111110": "姤卦",
    "011000": "萃卦",
    "000110": "升卦",
    "011010": "困卦",
    "010110": "井卦",
    "011101": "革卦",
    "101110": "鼎卦",
    "001001": "震卦",
    "100100": "艮卦",
    "110100": "漸卦",
    "001011": "歸妹卦",
    "001101": "豐卦",
    "101100": "旅卦",
    "110110": "巽卦",
    "011011": "兌卦",
    "110010": "渙卦",
    "010011": "節卦",
    "110011": "中孚卦",
    "001100": "小過卦",
    "010101": "既濟卦",
    "101010": "未濟卦",
}


# 卦象解析
HEXAGRAM_INTERPRETATIONS = {
    "乾卦": "第1卦 乾为天（乾）\n刚健中正 上上卦\n象曰：困龙得水好运交，不由喜气上眉梢，一切谋望皆如意，向后时运渐渐高。",
  "坤卦": "第2卦 坤为地（坤）\n柔顺伸展 大吉卦\n象曰：云从龙，风从虎，君子当安命守时，时运当来自然得。",
  "屯卦": "第3卦 水雷屯（屯）\n动难卦\n象曰：雷电交加风雨来，险难当前宜守成，心存忍耐好运来。",
  "蒙卦": "第4卦 山水蒙（蒙）\n启蒙卦\n象曰：日出山中破云霧，明光普照吉星臨，适合学问与启迪。",
  "需卦": "第5卦 水天需（需）\n需待卦\n象曰：虽在高原望遠天，風雨難遮去，未來机遇尽在眼前。",
  "訟卦": "第6卦 天水讼（讼）\n争讼卦\n象曰：天高水落分水处，口舌是非當慎思，化干戈为玉帛為妙。",
  "師卦": "第7卦 地水师（師）\n战争卦\n象曰：战车行远步步危，策马扬鞭当戒慎，不宜贸然取胜。",
  "比卦": "第8卦 水地比（比）\n和谐合作卦\n象曰：流水人家春盡處，團結力量能破难，亲密合作利人利己。",
  "小畜卦": "第9卦 风天小畜（小畜）\n小蓄卦\n象曰：天风拂地人安居，小有储蓄终成丰收，积少成多自能满愿。",
  "履卦": "第10卦 天泽履（履）\n慎行卦\n象曰：登高行险当知足，腳下须留神，踏实才能走得远。",
  "泰卦": "第11卦 地天泰（泰）\n天地交泰卦\n象曰：天与地相交融通，百事顺遂人心安，时运通畅自然吉祥。",
  "否卦": "第12卦 天地否（否）\n不通卦\n象曰：天地失合萬物闭，时运不通当谨慎，守静而待变，勿急躁。",
  "同人卦": "第13卦 天火同人（同人）\n同心同德卦\n象曰：火在天上普照明，同心协力谋事成，团结一致才有结果。",
  "大有卦": "第14卦 火天大有（大有）\n大富卦\n象曰：阳光普照万物荣，心怀宽广得富贵，机运盈满，宜多行善。",
  "謙卦": "第15卦 地山谦（谦）\n谦虚卦\n象曰：谦卑含德如山高，退而求进显高风，谦虚得福反而有益。",
  "豫卦": "第16卦 雷地豫（豫）\n快乐卦\n象曰：雷声震地喜事来，心怀快乐行事顺，欢乐有望顺利前行。",
  "隨卦": "第17卦 泽雷随（随）\n随从卦\n象曰：雷震万里泽水随，顺其自然勿固执，随波逐流前途无阻。",
  "蠱卦": "第18卦 山风蛊（蛊）\n修正卦\n象曰：山风吹动扰尘埃，修正过失防止错，宜反思改进。",
  "臨卦": "第19卦 地泽临（临）\n大吉卦\n象曰：天地佑人万物临，吉祥如意到眼前，凡事顺遂。",
  "觀卦": "第20卦 风地观（观）\n观察卦\n象曰：风拂大地观察妙，静观其变利自明，事宜缓而不急。",
  "噬嗑卦": "第21卦 火雷噬嗑（噬嗑）\n刑罚卦\n象曰：烈火雷鸣正刚中，破除阻碍化危机，刑罚才能守正义。",
  "賁卦": "第22卦 山火贲（贲）\n装饰卦\n象曰：烈火照耀山岭美，修饰外表增光彩，庄重外表也有道理。",
  "剝卦": "第23卦 山地剥（剥）\n剥落卦\n象曰：山石崩落土瓦覆，外强内虚易受损，小心谨慎为妙。",
  "復卦": "第24卦 地雷复（复）\n复兴卦\n象曰：雷声响震天地回，时运重来万事吉，失去的机会可再抓住。",
   "無妄卦": "第25卦 天雷无妄（无妄）\n无妄之灾卦\n象曰：雷霆万钧天不仁，无妄之灾不可避，保持本心，方得无妄。",
  "大畜卦": "第26卦 山天大畜（大畜）\n大蓄卦\n象曰：山高天远蓄势而动，积累实力未来可期，勿急躁，静待时机。",
  "頤卦": "第27卦 山雷颐（颐）\n自养卦\n象曰：山中有雷声阵阵，养身修心守正道，自足自养更为安稳。",
  "大過卦": "第28卦 泽风大过（大过）\n非常卦\n象曰：大木过江水滔滔，逆势而行，需避开极端，防止过度。",
  "坎卦": "第29卦 水坎（坎）\n险难卦\n象曰：险中行走不容易，心中有数才能过，勿轻举妄动。",
  "離卦": "第30卦 火离（离）\n光明卦\n象曰：火光辉煌照万物，光明前途可看见，正道而行，自有辉煌。",
  "咸卦": "第31卦 泽山咸（咸）\n感应卦\n象曰：山泽相通万物应，心灵相通人亦亲，感应之道利于合作。",
  "恆卦": "第32卦 雷风恒（恒）\n恒久卦\n象曰：风雷交加万年长，恒久之道方长久，坚守本心持之以恒。",
  "遯卦": "第33卦 天山遁（遁）\n退避卦\n象曰：天高山远宜退守，见机行事当远离，退守有益不必恋战。",
  "大壯卦": "第34卦 雷天大壮（大壮）\n壮大卦\n象曰：雷鸣天际声势壮，壮志凌云当勇猛，果敢决断，前途光明。",
  "晉卦": "第35卦 火地晋（晋）\n进步卦\n象曰：火烧原野红光遍，前程光明步步升，宜积极进取，前途无限。",
  "明夷卦": "第36卦 地火明夷（明夷）\n晦暗卦\n象曰：明灯遭覆光难现，黑暗时局当谨慎，守得云开见月明。",
  "家人卦": "第37卦 风火家人（家人）\n家道卦\n象曰：风吹火旺家庭兴，家道有序必安宁，和睦共处，家运昌隆。",
  "睽卦": "第38卦 火泽睽（睽）\n乖离卦\n象曰：火泽相离行不同，意见相左心不和，宜以包容化解矛盾。",
  "蹇卦": "第39卦 水山蹇（蹇）\n险阻卦\n象曰：山高水远行路难，前路艰险勿强求，待机而行，险阻自消。",
  "解卦": "第40卦 雷水解（解）\n解困卦\n象曰：雷震天地雨水降，困局解除现光明，困难化解，前景可期。",
  "損卦": "第41卦 山泽损（损）\n减损卦\n象曰：山高泽低互相损，舍小利以求大成，损益得失，贵在取舍。",
  "益卦": "第42卦 风雷益（益）\n增益卦\n象曰：风行雷动益万物，积极进取得丰收，利人利己，增益无限。",
  "夬卦": "第43卦 泽天夬（夬）\n决断卦\n象曰：水涨天高决心起，果断行事速见成，关键时刻勿拖泥带水。",
  "姤卦": "第44卦 天风姤（姤）\n遇合卦\n象曰：风行天上遇良机，机遇当前不可失，随机应变，积极把握。",
  "萃卦": "第45卦 泽地萃（萃）\n聚集卦\n象曰：水泽聚集万物齐，团结力量更强大，汇聚人心，众志成城。",
  "升卦": "第46卦 地风升（升）\n晋升卦\n象曰：风吹大地草木升，步步高升势头旺，前途无限，节节攀升。",
  "困卦": "第47卦 泽水困（困）\n困境卦\n象曰：水涸泽干困难多，身处困局不必慌，守静待变，困境自破。",
  "井卦": "第48卦 水风井（井）\n求才卦\n象曰：井水盈满润万物，潜龙在渊待时动，水源丰盈，才智待展。",
  "革卦": "第49卦 泽火革（革）\n变革卦\n象曰：烈火燃烧水上行，旧事推陈方可新，革新变革，机遇再现。",
  "鼎卦": "第50卦 火风鼎（鼎）\n鼎盛卦\n象曰：火燃鼎旺万事盛，鼎盛时期利百事，坚守根本，事业鼎盛。",
  "震卦": "第51卦 震为雷（震）\n震动卦\n象曰：雷声震动天地惊，行动果敢必成功，机遇当前迅速应对。",
  "艮卦": "第52卦 艮为山（艮）\n止步卦\n象曰：山势巍峨不动摇，止步守静方为妙，宜谨慎守成，不可妄动。",
  "漸卦": "第53卦 风山渐（渐）\n渐进卦\n象曰：风吹山岗事缓行，渐进之道方为上，凡事稳步前进为佳。",
  "歸妹卦": "第54卦 雷泽归妹（归妹）\n婚嫁卦\n象曰：雷泽相交姻缘成，婚姻和美事称心，结合时机当把握。",
  "豐卦": "第55卦 雷火丰（丰）\n丰盈卦\n象曰：雷火相交天地丰，丰收之时万物旺，吉星高照，丰盈有望。",
  "旅卦": "第56卦 火山旅（旅）\n旅途卦\n象曰：烈火山上孤行难，旅途奔波多辛苦，守静待时，旅途顺利。",
  "巽卦": "第57卦 巽为风（巽）\n顺风卦\n象曰：风行四方顺利达，凡事顺风顺水行，顺应时势，自然吉祥。",
  "兌卦": "第58卦 兑为泽（兑）\n喜悦卦\n象曰：泽水泛滥喜事多，心怀喜悦好事成，乐观自信，喜事临门。",
  "渙卦": "第59卦 风水涣（涣）\n涣散卦\n象曰：水流风散不成形，涣散局势难掌控，宜团结一致以应对。",
  "節卦": "第60卦 水泽节（节）\n节制卦\n象曰：泽水泛滥节制当，凡事有度需克制，节约自律，方得长久。",
  "中孚卦": "第61卦 风泽中孚（中孚）\n诚信卦\n象曰：风吹泽涌信义行，心怀诚信得人心，诚信为本，利于合作。",
  "小過卦": "第62卦 雷山小过（小过）\n过错卦\n象曰：雷鸣山间小过失，举措不当当改正，小错无妨，大错需防。",
  "既濟卦": "第63卦 水火既济（既济）\n既成卦\n象曰：水火相济事已成，凡事已成须守成，顺势而行，勿再冒进。",
  "未濟卦": "第64卦 火水未济（未济）\n未完成卦\n象曰：火水未济事未成，前路未竟需谨慎，步步为营，慎重应对。"
    # (添加更多解釋)
}

# 投擲銅錢，返回爻（陰或陽）及其是否為變爻
def toss_coin():
    result = [random.choice(["正面", "反面"]) for _ in range(3)]
    count_heads = result.count("正面")
    if count_heads == 3:
        return "老陽", "陽", "yang"
    elif count_heads == 2:
        return "少陽", "陽", "yang"
    elif count_heads == 1:
        return "少陰", "陰", "yin"
    else:
        return "老陰", "陰", "yin"

# 將爻轉為二進制字符串
def get_trigram_code(tosses):
    return ''.join(['1' if line == "陽" else '0' for line in tosses])

# 解析六爻為上下卦
def get_hexagram_codes(tosses):
    lower_trigram = get_trigram_code(tosses[:3])  # 下卦 (後三條爻)
    upper_trigram = get_trigram_code(tosses[3:])  # 上卦 (前三條爻)
    return lower_trigram, upper_trigram

# 繪製卦象圖像
def draw_lines(canvas, lines_display, labels, start_x, start_y, spacing):
    for idx, (line, label) in enumerate(zip(lines_display, labels)):
        y = start_y - idx * spacing
        if line == "yang":
            canvas.create_line(start_x, y, start_x + 120, y, width=2)
        else:
            canvas.create_line(start_x, y, start_x + 50, y, width=2)
            canvas.create_line(start_x + 70, y, start_x + 120, y, width=2)
        # 顯示爻的名稱
        canvas.create_text(start_x + 150, y, text=f"({label})", font=("Arial", 10))

# 顯示本卦和變卦結果
def show_hexagrams():
    global tosses, changing_lines, lines_display_original, lines_display_changed, labels_original

    # 計算變卦
    changed_tosses = []
    lines_display_changed = []  # 記錄變卦線條
    labels_changed = []
    for i, line in enumerate(tosses):
        if changing_lines[i]:
            changed_tosses.append("陰" if line == "陽" else "陽")
            labels_changed.append("老陰" if labels_original[i] == "老陽" else "老陽")
        else:
            changed_tosses.append(line)
            labels_changed.append(labels_original[i])
        # 記錄變卦線條
        lines_display_changed.append("yin" if line == "陽" and changing_lines[i] else "yang" if line == "陰" and changing_lines[i] else "yang" if line == "陽" else "yin")
    
    changed_lower_code, changed_upper_code = get_hexagram_codes(changed_tosses)

    # 計算六十四卦中的編號
    original_hexagram_index = HEXAGRAM_NAMES.get((get_trigram_code(tosses[3:])+ get_trigram_code(tosses[:3])))
    changed_hexagram_index = HEXAGRAM_NAMES.get((changed_upper_code+ changed_lower_code))

    # 顯示本卦與變卦名稱
    hexagram_display.set(f"本卦: 下卦 {TRIGRAM_NAMES.get(get_trigram_code(tosses[:3]))}, 上卦 {TRIGRAM_NAMES.get(get_trigram_code(tosses[3:]))} ({original_hexagram_index})\n"
                         f"變卦: 下卦 {TRIGRAM_NAMES.get(changed_lower_code)}, 上卦 {TRIGRAM_NAMES.get(changed_upper_code)} ({changed_hexagram_index})")
    
    # 繪製本卦和變卦線條
    draw_lines(canvas, lines_display_original, labels_original, 50, 400, 20)  # 繪製本卦
    draw_lines(canvas, lines_display_changed, labels_changed, 230, 400, 20)  # 繪製變卦

    # 在本卦和變卦下方添加標籤，並拉開兩組的距離
    canvas.create_text(110, 450, text="本卦", font=("Arial", 12))
    canvas.create_text(290, 450, text="變卦", font=("Arial", 12))

    # 顯示「查看解析」按鈕
    interpretation_button.pack(pady=10)

# 顯示卦象解析的頁面
def show_interpretation():
    result_frame.pack_forget()  # 隱藏結果頁面
    interpretation_frame.pack()  # 顯示解析頁面

    # 繪製本卦和變卦圖形
    draw_lines(interpretation_canvas, lines_display_original, labels_original, 50, 200, 20)  # 本卦
    draw_lines(interpretation_canvas, lines_display_changed, labels_changed, 230, 200, 20)  # 變卦

    # 顯示卦象名稱和解析
    original_hexagram_text.set(HEXAGRAM_INTERPRETATIONS.get(HEXAGRAM_NAMES.get((get_trigram_code(tosses[3:]) + get_trigram_code(tosses[:3]))), "無解釋"))
    changed_hexagram_text.set(HEXAGRAM_INTERPRETATIONS.get(HEXAGRAM_NAMES.get((changed_upper_code + changed_lower_code)), "無解釋"))

# 重置遊戲
def reset_game():
    global tosses, changing_lines, lines_display_original, lines_display_changed, labels_original
    tosses = []
    changing_lines = []
    lines_display_original = []
    lines_display_changed = []
    labels_original = []
    display_toss.set("")
    hexagram_display.set("")
    canvas.delete("all")
    interpretation_canvas.delete("all")
    start_frame.pack()
    result_frame.pack_forget()
    retry_button.pack_forget()
    toss_button.config(state=tk.NORMAL)

# 投擲過程並顯示結果
def toss_and_show():
    global tosses, changing_lines, lines_display_original, labels_original
    if len(tosses) < 6:
        result, final_line, visual_line = toss_coin()
        tosses.append(final_line)
        if result in ["老陽", "老陰"]:
            changing_lines.append(True)
        else:
            changing_lines.append(False)

        for _ in range(10):
            display_toss.set("投擲中...")
            root.update()
            time.sleep(0.05)
            display_toss.

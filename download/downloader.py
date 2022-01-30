import gspread

#define global variable
MSGCTXT = 0
MSGID = 1
TRANSLATION = 2

def extract_all_worksheet_as_list():
    gc = gspread.service_account(filename='../gspread/dst-TRANSLATION-56ed8e60ddc5.json')
    sh = gc.open("DST正體中文翻譯")
    worksheet_list = sh.worksheets()
    output = []
    for worksheet in worksheet_list:
        if worksheet.title in ["Discussion", "LUT", "mods", "梗&由來"]: #skip Discussion, LUT, mods, 梗&由來
            continue
        new_worksheet = worksheet.get_all_values()
        assert new_worksheet != None
        output.append(new_worksheet[2:])
    return output
#The output of above function will be list_of_all_worksheets in the next two function.
#list_of_all_worksheets is a list of lists. Elements in this list are the data of all worksheets except "Discussion".
#For example, list_of_all_worksheets[0] is the data of worksheet "其餘項目", list_of_all_worksheets[1] is the data of worksheet "Skin".
#The data of each worksheet will not include "ThePlayer.components.talker:Say("")" and the row of [msgctxt,	msgid, 翻譯, 谷哥說, 阿呆].
#For example, list_of_all_worksheets[0][0] is ['STRINGS.HERMITCRAB_COMPLAIN.FILL_MEATRACKS.HIGH.1', 'Could you dry some meat for me, dearie?', '你能幫我曬一些肉嗎，親愛的？', '', ''].
#You can check the data by calling print(list_of_all_worksheets[0][0]) in main function.
def build_dict_of_worksheets():
    list_of_all_worksheets = extract_all_worksheet_as_list()
    global MSGCTXT
    global MSGID
    global TRANSLATION
    output = []
    for worksheet in list_of_all_worksheets:
        dictionary = {}
        for data in worksheet:
            dictionary[data[MSGCTXT]] = [data[MSGID], data[TRANSLATION]]
        output.append(dictionary)
    return output #Each element of output is a dict of a worksheet

def build_whole_dict():
    list_of_all_worksheets = extract_all_worksheet_as_list()
    global MSGCTXT
    global MSGID
    global TRANSLATION
    dictionary = {}
    for worksheet in list_of_all_worksheets:
        for data in worksheet:
            dictionary[data[MSGCTXT]] = [data[MSGID], data[TRANSLATION]]
    return dictionary

if __name__ == '__main__':
    #list_of_all_worksheets = extract_all_worksheet_as_list()
    #print(list_of_all_worksheets[0][0])
    #list_of_all_dict_of_worksheets = build_dict_of_worksheets()
    #print(list_of_all_dict_of_worksheets[0]["STRINGS.ACTIONS.DECORATEVASE"])
    whole_dict = build_whole_dict()
    print(whole_dict["STRINGS.CHARACTERS.GENERIC.DESCRIBE.TROPHYSCALE_OVERSIZEDVEGGIES.HAS_ITEM"])





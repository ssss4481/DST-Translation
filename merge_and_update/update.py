import gspread
import merge_po as mp

def update_sheet():
    whole_dict, need_update_to_gsheet = mp.merge_gsheet_and_po()
    update_list = []

    for key in need_update_to_gsheet:
        value = need_update_to_gsheet[key]
        update_list.append([key, value[0].replace("\n","\\n"), value[1].replace("\n","\\n")])

    gc = gspread.service_account(filename='../gspread/dst-translation-912c8bbee315.json')
    sh = gc.open("DST正體中文翻譯")

    worksheet = None
    for wks in sh.worksheets():
        if wks.title == "New":
            worksheet = wks
            break

    assert worksheet != None
    worksheet.insert_rows(update_list, 3)

if __name__ == "__main__":
    update_sheet()
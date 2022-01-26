import polib
import os
import sys
sys.path.append('../download/')
import downloader

def recover():
    os.system("cp ../outputfile/chinese_copy.po ../outputfile/chinese_t.po")
    return

def merge_gsheet_and_po():
    os.system("cp ../outputfile/chinese_t.po ../outputfile/chinese_copy.po") #for redundant
    old_po = polib.pofile('../outputfile/chinese_t.po')
    whole_dict = downloader.build_whole_dict() #output to po
    need_update_to_gsheet = {} #which need to be update to gsheet
    for entry in old_po:
        if(entry.msgctxt not in whole_dict):
            whole_dict[entry.msgctxt] = [entry.msgid, entry.msgstr]
            need_update_to_gsheet[entry.msgctxt] = [entry.msgid, entry.msgstr]
    return whole_dict, need_update_to_gsheet

def output_po():
    whole_dict, need_update_to_gsheet = merge_gsheet_and_po()
    new_po = polib.POFile()
    new_po.metadata = {
        "Language":" zh",
        "Content-Type":" text/plain; charset=utf-8",
        "Content-Transfer-Encoding":" 8bit",
        "POT Version":" 2.0"
    }
    for key in sorted(whole_dict):
        entry = polib.POEntry(
            msgctxt = key,
            msgid= whole_dict[key][0],
            msgstr= whole_dict[key][1],
            occurrences=[('',key)]
        )
        new_po.append(entry)
    new_po.save('../outputfile/chinese_t.po')
    return











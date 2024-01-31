import re
from Ex20 import data_json as data
pattern_file = re.compile(r'''
        (?:File)   # Uncaptured, 'File' or 'ファイル'
        :
        (.+?)               # Capture target,
                            # 0 or more arbitrary characters,
                            # non-greedy match
        \|
        ''', re.VERBOSE)


res = pattern_file.findall(data)
for line in res:
    print(line)

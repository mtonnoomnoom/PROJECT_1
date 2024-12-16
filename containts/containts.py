
import os
CUR_DIRECTORY = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')
SRC_DIRECTORY = os.path.dirname(CUR_DIRECTORY)
DATA_FILE = SRC_DIRECTORY + "/data/Viet74K.txt"
DB_SRC=SRC_DIRECTORY+"/data/chromadb"
similar_pairs = [
    ('a', 'ă'), ('a', 'â'), ('ă', 'â'),  # Các biến thể của "a"
    ('e', 'ê'),                          # Các biến thể của "e"
    ('o', 'ô'), ('o', 'ơ'), ('ô', 'ơ'),  # Các biến thể của "o"
    ('u', 'ư'),                          # Các biến thể của "u"
    ('d', 'đ'),                          # "d" và "đ"
    ('i', 'y'),                          # "i" và "y"
    ('s', 'x'),                          # "s" và "x" (hay nhầm do âm phát)
    ('n', 'm'),                          # "n" và "m" (lỗi gõ)
    ('t', 'th'),                         # "t" và "th" (âm gần)
    ('c', 'k'),                          # "c" và "k" (cùng âm đầu trong nhiều trường hợp)
    ('g', 'gh'),                         # "g" và "gh" (âm đầu)
    ('ng', 'ngh'),                       # "ng" và "ngh" (cặp tương tự về ngữ âm)
    ('h', 'k'),                          # "h" và "k" (hay nhầm do lỗi OCR)
    ('u', 'v'),                          # "u" và "v" (nhầm do hình dạng tương tự)
    ('o', '0'),                          # "o" và số "0" (nhầm lẫn phổ biến)
    ('l', '1'),                          # "l" và số "1"
    ('i', 'l'),                          # "i" và "l" (lỗi OCR)
    ('r', 'd'),                          # "r" và "d" (phát âm địa phương)
    ('g', 'q'),                          # "g" và "q" (hình dạng gần giống)
    ('p', 'q'),                          # "p" và "q" (do hình dạng)
    ('a', 'e'),                          # "a" và "e" (phát âm nhầm lẫn trong một số ngữ cảnh)
    ('t', 'l'),                          # "t" và "l" (phát âm địa phương)
    ('b', 'v')                           # "b" và "v" (hay nhầm trong phát âm)
]

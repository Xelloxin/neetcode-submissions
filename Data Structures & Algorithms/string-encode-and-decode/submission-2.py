# class Solution:

#     def encode(self, strs: List[str]) -> str:
#         if not strs:
#             return ""

#         encode= []
#         for word in strs:
#             length = len(word)
#             a = '-'.join(str(ord(v)*length) for v in word)
#             encode.append(a)
#         return "/".join(encode)

#     def decode(self, s: str) -> List[str]:
#         if not s:
#             return []
#         decode = []
#         encoded = s.split("/")
#         for st in encoded:
#             if not st:
#                 decode.append("")
#                 continue
#             cha = [int(x) for x in st.split('-')]
#             w = ''.join(chr(x//len(cha)) for x in cha)
#             decode.append(w)
#         return decode

from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "EMPTY_LIST"
            
        encode_list = []
        for word in strs:
            length = len(word)
            a = '-'.join(str(ord(v) * length) for v in word)
            encode_list.append(a)
        return "/".join(encode_list)

    def decode(self, s: str) -> List[str]:
        if s == "EMPTY_LIST":
            return []
            
        decode_list = []
        encoded = s.split("/")
        
        for st in encoded:
            if not st:
                decode_list.append("")
                continue
                
            cha = [int(x) for x in st.split('-')]
            w = ''.join(chr(x // len(cha)) for x in cha)
            decode_list.append(w)
            
        return decode_list




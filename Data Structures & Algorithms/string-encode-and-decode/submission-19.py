class Solution:

    def encode(self, strs: List[str]) -> str:
        #format: {len_str+str+len_str+str+0}
        encoded_str = ""
        for s in strs:
            s_len = len(s)
            encoded_str = encoded_str+ f"{s_len}x" + s
        return encoded_str


    def decode(self, s: str) -> List[str]:
        i=0
        decoded_strs = []
        while i < len(s):
            length =""
            while s[i] != 'x':
                length += s[i]
                i+=1
            decoded_strs.append(s[i+1:i+1+int(length)])
            i= i+1+int(length)
        return decoded_strs

class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "Nothing"
        if len(strs) == 1:
            return strs[0]

        s = "🐍".join(strs)
        return s

    def decode(self, s: str) -> List[str]:
        if s == "Nothing":
            return []
        if not s:
            return [s]
        ss = s.split("🐍")
        return ss

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        def get(c):
            return ord(c) - ord('a')

        w = 100
        lines = 1
        width = 0
        for c in s:
            neo = widths[get(c)]
            if width+neo > w:
                lines += 1
                width = neo
            else:
                width += neo
        return [lines, width]
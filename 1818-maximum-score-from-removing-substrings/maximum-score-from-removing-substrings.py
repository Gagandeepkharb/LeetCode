class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pair(s: str, a: str, b: str, score: int) -> tuple[str, int]:
            stack = []
            total = 0
            for char in s:
                if stack and stack[-1] == a and char == b:
                    stack.pop()
                    total += score
                else:
                    stack.append(char)
            return ''.join(stack), total

        total_score = 0
        if x >= y:
            s, score_x = remove_pair(s, 'a', 'b', x)
            s, score_y = remove_pair(s, 'b', 'a', y)
        else:
            s, score_y = remove_pair(s, 'b', 'a', y)
            s, score_x = remove_pair(s, 'a', 'b', x)

        total_score = score_x + score_y
        return total_score

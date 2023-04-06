"""
Approach: Ad-hoc
Time Complexity: O(Kx2^N)
Space Complexity: O(Kx2^N)
"""

def main():
    text = input()
    n = int(input())
    clipboard = []
    for _ in range(n):
        command, *args = input().split()
        if command == "COPY":
            start, end = map(int, args)
            clipboard += [text[start-1:end]]
        elif command == "CUT":
            start, end = map(int, args)
            clipboard += [text[start-1:end]]
            text = text[:start-1] + text[end:]
        elif command == "PASTE":
            start = int(args[0])
            text = text[:start-1] + clipboard[-1] + text[start-1:]
            if len(clipboard) > 1:
                clipboard.pop()
    return text


if __name__ == '__main__':
    main()

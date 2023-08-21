class LongestPalindrome:
    """
    Find the longest palindromic substring.
    """

    def longest_palindrome(self, string: str) -> str:
        """
        Returns the longest palindromic substring for the given string.
        """
        longest = ""
        length = len(string)
        for i, _ in enumerate(string):
            center = i
            radius = 1
            # Odd palindrome
            while (
                (center - radius >= 0)
                and (center + radius < length)
                and (string[center - radius] == string[center + radius])
            ):
                radius += 1
            radius -= 1
            odd_palindrome = string[(center - radius) : (center + radius + 1)]
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            # Even palindrome
            if i > 0 and (string[i] == string[i - 1]):
                left = i - 1
                right = i
                while (
                    (left - 1 >= 0)
                    and (right + 1 < length)
                    and (string[left - 1] == string[right + 1])
                ):
                    right += 1
                    left -= 1
                even_palindrome = string[left : (right + 1)]
                if len(even_palindrome) > len(longest):
                    longest = even_palindrome
            if (i + 1) < len(string) and (string[i] == string[i + 1]):
                left = i
                right = i + 1
                while (
                    (left - 1 >= 0)
                    and (right + 1 < length)
                    and (string[left - 1] == string[right + 1])
                ):
                    right += 1
                    left -= 1
                even_palindrome = string[left : (right + 1)]
                if len(even_palindrome) > len(longest):
                    longest = even_palindrome
        return longest

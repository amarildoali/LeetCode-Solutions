class Solution {
    public boolean isPalindrome(int x) {
        String s = String.valueOf(x);
        int head = 0;
        int tail = s.length() - 1;

        while (head < tail) {
            if (s.charAt(head++) != s.charAt(tail--)) {
                return false;
            }
        }
        return true;
    }
}

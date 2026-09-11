class Solution {
    public boolean isPalindrome(String s) {
            String ns = "";

            for (char c : s.toCharArray()){
                if (Character.isDigit(c) || Character.isLetter(c)){
                    ns += c;
                }
            }

            ns = ns.toLowerCase();

            int a = 0;
            int b = ns.length() - 1;

            while (a <= b){
                if (ns.charAt(a) != ns.charAt(b)){
                    return false;
                }

                a++;
                b--;
            }

            return true;
    }
    
}


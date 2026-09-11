class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> map = new HashMap<>();

        if ( s.length() != t.length()){
             return false;
        }

        for (char x : s.toCharArray()){
            map.put(x, map.getOrDefault(x, 0) + 1);
        }

        for (char x : t.toCharArray()){
            map.put(x, map.getOrDefault(x, 0) - 1);
        }
        

        for (Map.Entry<Character, Integer> entry : map.entrySet()){
            if (entry.getValue() != 0){
                return false;
            }
            
        }
        return true;
    }
}

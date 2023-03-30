class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        HashMap<Character, Character> map = new HashMap<Character, Character>();
        map.put('(', ')');
        map.put('{', '}');
        map.put('[', ']');
        
        for (char curr : s.toCharArray()) {
            if (map.containsKey(curr)) {
                stack.push(curr);
            } else {
                if (stack.size() != 0 && curr == map.get(stack.peek())) {
                    stack.pop();
                } else {
                    return false;   
                }
            }
        }
        
        if (stack.size() == 0) return true;
        return false;
    }
}
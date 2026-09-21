import java.util.Stack;

class Solution { 
    public boolean isValid(String s) { 
        Stack<Character> st = new Stack<Character>(); 
        
        for (int i = 0; i < s.length(); i++) { 
            char a = s.charAt(i); 
            
            if (a == '(' || a == '[' || a == '{') { 
                st.push(a); 
            } else { 
                if (st.isEmpty()) return false; 
                
                char top = st.pop(); 
                // Fixed the typo in the third condition below
                if ((a == ')' && top != '(') || (a == ']' && top != '[') || (a == '}' && top != '{')) { 
                    return false; 
                } 
            } 
        } 
        // Fixed to ensure no unclosed brackets remain in the stack
        return st.isEmpty(); 
    } 
}

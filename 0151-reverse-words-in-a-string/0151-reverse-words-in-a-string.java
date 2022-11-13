class Solution {
    public String reverseWords(String s) {
        String revStr = "";
        // Trim white spaces from the start and end of string.
        s = s.trim();
        // Replace all spaces (no matter the length) with a single space.
        s = s.replaceAll("\s+", " ");
        // Split string into array of words.
        String [] wordsInS = s.trim().split(" ");
        // Run a reverse loop of the array to add words to revStr.
        for(int i = wordsInS.length; i>0; i--){
            revStr += wordsInS[i-1];
            // Don't add a space if we are on the final word.
            if(i != 1)
                revStr += " ";
        }
        return revStr;
    }
}
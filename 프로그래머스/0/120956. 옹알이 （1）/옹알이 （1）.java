class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        String[] canSay = {"aya", "ye", "woo", "ma"};

        for (String word : babbling) {
            String temp = word;
            for (String say : canSay) {
                temp = temp.replaceFirst(say, " ");
            }
            if (temp.replace(" ", "").equals("")) {
                answer++;
            }
        }

        return answer;
    }
}
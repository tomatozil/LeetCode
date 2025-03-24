class Solution {
    public boolean isAnagram(String s, String t) {
        List<String> sList = Arrays.asList(s.split(""));
        List<String> tList = Arrays.asList(t.split(""));
        Collections.sort(sList);
        Collections.sort(tList);

        if (sList.equals(tList))
            return true;
        return false;
    }
}

class Solution {
    public int climbStairs(int n) {
        if(n==1 || n==2 || n==3){
            return n;
        }
        int prevStep = 3;
        int secondLastStep = 2;
        int currStep = 0;

        for(int i = prevStep; i<n;i++){
            currStep = prevStep + secondLastStep;
            secondLastStep = prevStep;
            prevStep = currStep;
        }
        return currStep;
    }
}
public class fib_java {
    /*  쳲���������
        Fibonacci(40)=102334155
        ����Fibonacci��ʱ --> 422ms
    */
    private static int fib(int n) {
        if (n<2){
            return n;
        }
        return fib(n - 1) + fib(n - 2);
    }

    public static void main(String[] args) {
        long startTime = System.currentTimeMillis();
        int fibN = 40;
        int n = fib(fibN);
        long endTime = System.currentTimeMillis();    
        System.out.printf("Fibonacci(%d)=%d\n",fibN, n);
        System.out.println("����Fibonacci��ʱ --> " + (endTime - startTime) + "ms");
    }
}

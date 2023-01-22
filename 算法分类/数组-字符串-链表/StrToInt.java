public class StrToInt {

    // Assume int is 4 bytes
    public static int strToInt(String str) {
        int i = 0, num = 0;
        boolean isNeg = false;
        int len = str.length();

        if (len > 10) {
            System.out.println("Out of Scope!");
            return 0;
        }

        // 判断是否为signed int
        if (str.charAt(0) == '-') {
            isNeg = true;
            i = 1;
        }

        // 将char转为字面数字, 从左向右遍历, 可以省去一步乘法
        while (i < len) {
            num *= 10;
            num += (str.charAt(i++) - '0');
        }
        if (isNeg)
            num = -num;

        return num;
    }

    public static void main(String[] args) {
        int result = StrToInt.strToInt("888888");

        System.out.println(result);
    }
}
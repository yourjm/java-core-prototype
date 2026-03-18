package tasks.arrays;

public class EvenElements {

    /**
     * Возвращает новый массив содержащий только чётные элементы.
     *
     * Пример:
     *   вход:  [1, 2, 3, 4, 5, 6]
     *   выход: [2, 4, 6]
     */
    public static int[] getEven(int[] input) {
        int[] temp = new int[100];
        int count = 0;
        for (int i = 0; i < input.length; i++) {
            if (input[i] % 2 == 0) {
                temp[count] = input[i];
                count++;
            }
        }
        int[] result = new int[count];
        for (int i = 0; i < count; i++) {
            result[i] = temp[i];
        }
        return result;
    }
}
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
        return Arrays.stream(input)
                .filter(n -> n % 2 == 0)
                .toArray();
    }
}
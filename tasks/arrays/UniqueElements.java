package tasks.arrays;

public class UniqueElements {

    /**
     * Возвращает новый массив с уникальными элементами в том же порядке.
     *
     * Пример:
     *   вход:  [1, 2, 2, 3, 1]
     *   выход: [1, 2, 3]
     */
    public static int[] getUnique(int[] input) {
        int[] temp = new int[input.length];
        int count = 0;
        for (int i = 0; i < input.length; i++) {
            boolean found = false;
            for (int j = 0; j < count; j++) {
                if (temp[j] == input[i]) {
                    found = true;
                    break;
                }
            }
            if (!found) {
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

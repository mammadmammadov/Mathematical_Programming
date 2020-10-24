import java.util.Scanner;

public class ConvertFromDecimalToBinary {

	public static void main(String[] args) {
		int number;
		int iteration = 0;
		int[] array = new int[25];
		Scanner in = new Scanner(System.in);
		System.out.print("Input a decimal number: ");
		number = in.nextInt();
		while (number >= 1) {
			array[iteration++] = (int) (number % 2);
			number = number / 2;
		}
		iteration = iteration - 1;
		System.out.print("Binary number is: ");
		while (iteration >= 0) {

			System.out.print(array[iteration--]);
		}

	}

}

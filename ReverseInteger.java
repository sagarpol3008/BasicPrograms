import java.util.Scanner;

public class ReverseInteger {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int reverse = 0;
		System.out.println("Enter Number: ");
		int number = sc.nextInt();
		
		while(number != 0)   
		{  
		int remainder = number % 10;  
		reverse = reverse * 10 + remainder;  
		number = number/10;  
		}  
		System.out.println("The reverse of the given number is: " + reverse);  


	}

}

import java.util.Scanner;

public class ReverseString {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String str;  
		Scanner sc=new Scanner(System.in);  
		System.out.print("Enter a String: ");  
		str=sc.nextLine();                      
		System.out.print("Reverse string is: ");  
		for(int i=str.length();i>0;--i)                 
		{  
		System.out.print(str.charAt(i-1));           
		}  

	}

}

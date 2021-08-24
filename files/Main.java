import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;




public class Main {
	public static void main(String[] args) {


		//Creates a HashMap of each target function, along with spacing adjustments for esthetic purposes.
		HashMap<String, String> functions = new HashMap<String, String>();

		functions.put("0$x$", "/1");
		functions.put("1$x^2-4$", "/2");
		functions.put("2$x^2-1$", "/2");


		//... There should be one more function above as there are lines of values below.

		//Creates a List of values each function will take for each section. Values will be different for tables of signs (LIN) and tables of variation (VAR).
			// For LIN : a space means there will be nothing (between or on), - is a minus (between), + is a plus (between), z is a zero (on), h is a barred zone, d is a double-line (on).
			// For VAR : a space
		List<String> values = new ArrayList<String>();
		values.add("LIN, , +, 0, -, , -, , -, 0, +, ");
		values.add("LIN, , +, , +, 0, -, 0, +, , +, ");
		//Creates horizontal sections for default target values.
		List<String> sections = List.of("$-\\infty$, $-2$, $-1$, $ 1$, $ 2$, $+\\infty$");


		//Creates a TikzPicture image with global rescaling and custom spacing inside the table.
		TikzText image = new TikzText();
		image.setCustomSpace(2);
		Table table = new Table(functions, sections, values);
		image.printTable(table, true);

	}
}

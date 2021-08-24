import java.util.List;
import java.util.HashMap;

public class Table {
	private HashMap<String, String> functions;
	private List<String> sections;
	private List<String> values;
	
	public Table(HashMap<String, String> functions, List<String> sections, List<String> values) {
		this.functions = functions;
		this.sections = sections;
		this.values = values;
	}
	
	public HashMap<String, String> getFunctions() {
		return functions;
	}
	
	public List<String> getSections() {
		return sections;
	}
	
	public List<String> getValues() {
		return values;
	}
}

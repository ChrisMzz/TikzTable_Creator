import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class TikzText {
	
	private String scale = "";
	private double customSpace;
	
	
	
	public TikzText(double scale) {
		this.scale = "[scale=" + scale + "]";
	}
	
	public TikzText() {
	}
	
	
	public void setCustomSpace(double space) {
		this.customSpace = space;
	}
	
	public double getCustomSpace() {
		return customSpace;
	}
	
	
	public String printTable(Table table, boolean customSpaceBool) {
		List<String> functionsKeyList = new ArrayList<String>();
		for (String element : table.getFunctions().keySet()) {
			functionsKeyList.add(element);
		}
		Collections.sort(functionsKeyList);
		
		
		
		String tempText = "";
		
		tempText += "\\begin{tikzpicture}" + scale + "\n";
		
		tempText += "\\tkzTabInit";
		
		tempText += (customSpaceBool) ? "[espcl=" + customSpace + "]" : "";
		
		tempText += "{";
		for (String element : functionsKeyList) {
			tempText += element.substring(1,element.length()) + " " + table.getFunctions().get(element) + ", ";
		}
		tempText = tempText.substring(0, tempText.length()-2) + "}";
		
		tempText += "{";
		for (String element : table.getSections()) {
			tempText += element + ", ";
		}
		tempText = tempText.substring(0, tempText.length()-2) + "}\n";
		
		for (String element : table.getValues()) {
			tempText += (element.substring(0,3).equals("LIN")) ? "\\tkzTabLine{" + element.substring(4,element.length()) + "}\n" : "\\tkzTabVar{" + element.substring(4,element.length()) + "}\n";
		}	
			
		
		tempText += "\\end{tikzpicture}\n";	
		System.out.println(tempText);
		return tempText;
	}
	
	

	
	
}

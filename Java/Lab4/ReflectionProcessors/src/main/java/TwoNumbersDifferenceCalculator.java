import javafx.scene.control.Label;

import java.util.ArrayList;

public class TwoNumbersDifferenceCalculator implements Processor{
    private String result = "";
    private int taskId = 0;

    public boolean submitTask(String task, StatusListener sl, Label label) {
        sl = new MyStatusListener(); //bad style
        taskId ++;
        simulateDelationOfWork(sl, label, taskId);
        String[] str = task.split(";");
        ArrayList<Integer> ar = new ArrayList<>();
        try {
            for (int i = 0; i < str.length; i++) {
                ar.add(Integer.parseInt(str[i]));
            }
        }catch (NumberFormatException e){
            result = "Exception occured";
            return false;
        }
        if(ar.size() != 2){
            result = "Exactly two numbers are required";
            return false;
        }
        Integer res = ar.get(0) - ar.get(1);
        result = res.toString();
        return true;
    }

    @Override
    public String getInfo() {
        return new String("Obliczanie różnicy liczb\nPrzykładowe dane wejściowe algorytmu:\n7;5");
    }

    @Override
    public String getResult() {
        return this.result;
    }
}

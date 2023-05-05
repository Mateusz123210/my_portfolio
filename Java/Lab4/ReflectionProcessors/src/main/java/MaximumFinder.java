import javafx.scene.control.Label;

import java.util.ArrayList;

public class MaximumFinder implements Processor{
    private String result = "";
    private int taskId = 0;

    @Override
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
        if(ar.size() == 0){
            result = "No numbers found";
            return false;
        }
        Integer max = ar.get(0);
        for(int i = 0; i < ar.size(); i++){
            if(ar.get(i) > max) max = ar.get(i);
        }
        result = max.toString();
        return true;
    }

    @Override
    public String getInfo() {
        return new String("Wyszukiwanie największej liczby\nPrzykładowe dane wejściowe algorytmu:\n" +
                "15;24;32;11;14;51;62"
        );
    }

    @Override
    public String getResult() {
        return this.result;
    }
}

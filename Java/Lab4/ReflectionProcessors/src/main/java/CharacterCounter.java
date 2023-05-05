import javafx.scene.control.Label;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class CharacterCounter implements Processor{
    private String result = "";
    private int taskId = 0;

    @Override
    public boolean submitTask(String task, StatusListener sl, Label label) {
        sl = new MyStatusListener(); //bad style
        taskId ++;
        simulateDelationOfWork(sl, label, taskId);
        if(task == null || task.length() == 0){
            result = "Write string first";
            return false;
        }
        Map<String, Integer> charactersMap = new HashMap<>();
        for(int i = 0; i < task.length(); i++){
            String a = String.valueOf(task.charAt(i));
            if(charactersMap.containsKey(a)){
                charactersMap.put(a, charactersMap.get(a) + 1);
            }else{
                charactersMap.put(a, 1);
            }
        }
        result = charactersMap.toString();
        return true;
    }

    @Override
    public String getInfo() {
        return new String("Obliczanie liczby znaków w tekście\nPrzykładowe dane wejściowe algorytmu:\n" +
                "Ala ma kota 123"
        );
    }

    @Override
    public String getResult() {
        return this.result;
    }
}

import javafx.scene.control.Label;

public class StringComparator implements Processor{
    private String result = "";
    private int taskId = 0;

    @Override
    public boolean submitTask(String task, StatusListener sl, Label label) {
        sl = new MyStatusListener(); //bad style
        taskId ++;
        simulateDelationOfWork(sl, label, taskId);
        if(task == null || task.length() == 0){
            result = "Write two strings first";
            return false;
        }
        String[] str = task.split(";");
        if(str.length != 2){
            result = "Write String in valid format";
            return false;
        }
        boolean res = str[0].equals(str[1]);
        result = String.valueOf(res);
        return true;
    }

    @Override
    public String getInfo() {
        return new String("Porównywanie ciągów znaków\nPrzykładowe dane wejściowe algorytmu:\nabcdef;abcdef");
    }

    @Override
    public String getResult() {
        return this.result;
    }
}

package pl.edu.pwr.weakreferenceslibrary;

import javafx.scene.control.TreeView;
import javafx.stage.Stage;

public class WeakReferencesMain {
    private DirectoryChanger dc;

    private TreeConstructor tc;

    private FileDataGetterInterface dg;
    public WeakReferencesMain(){
        dc = new DirectoryChanger();
        tc = new TreeConstructor();
        dg = new FileDataGetter();
    }

    public void chooseDirectory(Stage stage){
        String actualPath = dc.changeDirectory(stage);
        if(actualPath.length() > 0){
            tc.createTreeView(actualPath);
        }else{
            tc.clearTree();
        }
    }
    public String getCurrentDirectory(){
        return dc.getDirectory();
    }

    public TreeView getCurrentTree(){
        return tc.getTree();
    }
    public FileData readFileData(String path){
        return dg.readFileAndCalculateAverages(path);
    }

}

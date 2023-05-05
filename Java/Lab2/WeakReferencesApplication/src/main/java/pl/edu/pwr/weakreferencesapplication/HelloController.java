package pl.edu.pwr.weakreferencesapplication;

import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;
import pl.edu.pwr.weakreferenceslibrary.FileData;
import pl.edu.pwr.weakreferenceslibrary.WeakReferencesMain;

public class HelloController {

    private WeakReferencesMain mainLibrary = new WeakReferencesMain();

    @FXML
    private TreeView directoriesTree;

    @FXML
    private TextField chosenDirectory;

    @FXML
    private TextField averagePressure;

    @FXML
    private TextField averageTemperature;

    @FXML
    private TextField averageHumidity;

    @FXML
    private Label placeOfGetLabel;

    @FXML
    private TextArea preview;

    @FXML
    private AnchorPane ap;
    private boolean occupied = false;

    public HelloController(){
        super();
        directoriesTree = new TreeView();
    }

    private synchronized boolean setOccupied(boolean value){
        if (value == false){
            occupied = false;
            return true;
        }else{
            if(occupied == true){
                return false;
            }else{
                occupied = true;
                return true;
            }
        }
    }
    @FXML
    protected void onChooseButtonClick() {
        if(setOccupied(true)){
            Stage stage = (Stage) ap.getScene().getWindow();
            mainLibrary.chooseDirectory(stage);
            chosenDirectory.setText(mainLibrary.getCurrentDirectory());
            preview.setText("");
            averagePressure.setText("");
            averageTemperature.setText("");
            averageHumidity.setText("");
            placeOfGetLabel.setText("");
            TreeView returnedTree = mainLibrary.getCurrentTree();
            if (returnedTree != null){
                directoriesTree.setRoot(returnedTree.getRoot());
                directoriesTree.getSelectionModel().selectedItemProperty().addListener(new ChangeListener<TreeItem<String>>() {
                    @Override
                    public void changed(ObservableValue<? extends TreeItem<String>> observableValue, TreeItem<String> stringTreeItem, TreeItem<String> t1) {
                        if(setOccupied(true)) {
                            if (t1 != null && t1.getChildren().size() == 0 && t1.getParent() != null) {
                                StringBuilder s = new StringBuilder();
                                s.append(t1.getValue());
                                TreeItem it = t1;
                                while (it.getParent() != null) {
                                    it = it.getParent();
                                    if (it.getParent() != null)
                                        s.insert(0, it.getValue() + "\\");
                                }
                                s.insert(0, "\\");
                                s.insert(0, mainLibrary.getCurrentDirectory());
                                FileData fd = mainLibrary.readFileData(s.toString());
                                if (fd != null){
                                    preview.setText(fd.getPreview());
                                    averagePressure.setText(fd.getAveragePressure());
                                    averageTemperature.setText(fd.getAverageTemperature());
                                    averageHumidity.setText(fd.getAverageHumidity());
                                    if(fd.getFromFile() == true){
                                        placeOfGetLabel.setText("Loaded from file");
                                    }else{
                                        placeOfGetLabel.setText("Loaded from WeakHashMap");
                                    }
                                }else{
                                    placeOfGetLabel.setText("File has not been loaded!");
                                }
                            }
                            setOccupied(false);
                        }
                    }
                });
            }else{
                directoriesTree.setRoot(new TreeView().getRoot());
            }

            setOccupied(false);
        }
    }
}
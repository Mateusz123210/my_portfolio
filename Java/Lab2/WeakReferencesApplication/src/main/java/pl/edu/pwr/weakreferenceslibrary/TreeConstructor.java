package pl.edu.pwr.weakreferenceslibrary;

import javafx.scene.control.TreeItem;
import javafx.scene.control.TreeView;
import javafx.scene.image.ImageView;

import java.io.File;
import java.io.IOException;
import java.nio.file.DirectoryStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class TreeConstructor {
    private TreeView treeView;

    private Integer imageNumber = 1;

    public TreeView getTree(){
        return treeView;
    }
    public void clearTree(){
        this.treeView = new TreeView();
    }


    public TreeView createTreeView(String dirPath) {
        treeView = new TreeView();
        TreeItem<Object> tree = new TreeItem<>(dirPath.substring(dirPath.lastIndexOf(File.separator) + 1), new ImageView());
        List<TreeItem<Object>> dirs = new ArrayList<>();
        try {
            DirectoryStream<Path> directoryStream = Files.newDirectoryStream(Paths.get(dirPath));
            for (Path path : directoryStream) {
                if (Files.isDirectory(path)) {
                    String pathString = path.toString();
                    TreeItem<Object> subDirectory = new TreeItem<>(pathString.substring(pathString.lastIndexOf(File.separator) + 1), new ImageView());
                    getSubLeafs(path, subDirectory);
                    dirs.add(subDirectory);
                }
                else{
                    String pathString = path.toString();
                    TreeItem<Object> subFile = new TreeItem<>(pathString.substring(pathString.lastIndexOf(File.separator) + 1), new ImageView());
                    dirs.add(subFile);
                }
            }

            tree.getChildren().addAll(dirs);
        } catch (IOException e) {
            return null;
        }

        treeView.getSelectionModel().selectedItemProperty().addListener((obs, oldVal, newVal) -> {
            imageNumber = 1;
            StringBuilder pathBuilder = new StringBuilder();
            for (TreeItem<String> item = (TreeItem<String>) treeView.getSelectionModel().getSelectedItem(); item != null; item = item.getParent()) {

                pathBuilder.insert(0, item.getValue());
                pathBuilder.insert(0, "/");
            }
            String path = pathBuilder.toString();
        });
        tree.setExpanded(true);
        treeView.setRoot(tree);
        treeView.setShowRoot(true);
        return treeView;
    }

    private void getSubLeafs(Path subPath, TreeItem<Object> parent) throws IOException{

            DirectoryStream<Path> directoryStream = Files.newDirectoryStream(Paths.get(subPath.toString()));
            for (Path subDir : directoryStream) {
                if (Files.isDirectory(subDir)) {
                    String subTree = subDir.toString();
                    TreeItem<Object> subLeafs = new TreeItem<>(subTree, new ImageView());
                    subLeafs.setValue(subTree.substring(subTree.lastIndexOf(File.separator) + 1));
                    getSubLeafs(subDir, subLeafs);
                    parent.getChildren().add(subLeafs);
                }else{
                    String subTree = subDir.toString();
                    TreeItem<Object> subLeafs = new TreeItem<>(subTree, new ImageView());
                    subLeafs.setValue(subTree.substring(subTree.lastIndexOf(File.separator) + 1));
                    parent.getChildren().add(subLeafs);
                }
            }

    }
}

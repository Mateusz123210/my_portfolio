package pl.edu.pwr.filesMD5SnapshotLibrary;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.stream.Stream;
//Function finds all files in directory
public class FilesSearch {
    public ArrayList<String> getFilesPathsInDirectoryAndSubdirectories(String directoryPath) throws IOException {
        ArrayList<String> filesPaths = new ArrayList<>();
        Stream<Path> allObjects = Files.list(Paths.get(directoryPath));
        allObjects.forEach(path -> {
            if (!Files.isDirectory(path)) {
                filesPaths.add(path.toString());
            }
        });
        return filesPaths;
    }

    public static void main(String[] args) throws IOException {
        FilesSearch search = new FilesSearch();
        ArrayList<String> ar = search.getFilesPathsInDirectoryAndSubdirectories("C:\\Users\\mateu\\Desktop");
        for (String a: ar) {
            System.out.println(a);
        }
        System.out.println(ar.size());
    }
}

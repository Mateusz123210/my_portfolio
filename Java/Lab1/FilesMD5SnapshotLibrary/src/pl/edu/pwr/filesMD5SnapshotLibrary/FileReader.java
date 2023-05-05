package pl.edu.pwr.filesMD5SnapshotLibrary;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class FileReader {

    //Function reads file to byte array
    public byte[] getFileBytes(String path) {
        Path nioPath = Paths.get(path);
        byte[] fileContent;
        try {
            fileContent = Files.readAllBytes(nioPath);
        } catch (IOException e) {
            return null;
        }
        return fileContent;
    }
}

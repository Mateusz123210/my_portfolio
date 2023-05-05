package pl.edu.pwr.filesMD5SnapshotLibrary;

import org.apache.commons.lang3.SerializationUtils;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.NoSuchFileException;
import java.nio.file.Paths;
import java.util.HashMap;
public class Snapshot {
    //Function reads snapshot from file
    public HashMap<String, String> readSnapshotfromFile(String directoryPath) throws IOException {
        String userCatalog = System.getProperty("user.home");
        String path = userCatalog + "\\" + directoryPath.replace("\\", "").replace(":", "") +
                ".snapshot";
        byte [] readedFromFile;
        try{
           readedFromFile = Files.readAllBytes(Paths.get(path));
        }catch(NoSuchFileException ex){
            return null;
        }
        HashMap<String, String> deserialized = SerializationUtils.deserialize(readedFromFile);
        return deserialized;
    }
    //Function saves snapshot to file
    public Boolean writeSnapshotToFile(String directoryPath, HashMap<String, String> newSnapshot){
        String userCatalog = System.getProperty("user.home");
        String path = userCatalog + "\\" + directoryPath.replace("\\", "").replace(":", "") +
                ".snapshot";
        byte [] snapshotBytes = SerializationUtils.serialize(newSnapshot);
        try {
            Files.write(Paths.get(path), snapshotBytes);
        } catch (IOException e) {
            return false;
        }
        return true;
    }
}

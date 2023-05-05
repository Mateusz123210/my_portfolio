package pl.edu.pwr.weakreferenceslibrary;

@FunctionalInterface
public interface FileDataGetterInterface {
    public FileData readFileAndCalculateAverages(String path);
}
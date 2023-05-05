package pl.edu.pwr.weakreferenceslibrary;


import java.util.List;
import java.util.WeakHashMap;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class FileDataGetter implements FileDataGetterInterface, FileReaderInterface{
    private WeakHashMap<String, FileData> weakHashMap;

    private FileReaderInterface fileReader;

    public FileDataGetter(){
        weakHashMap = new WeakHashMap<>();
        fileReader = new FileReaderInterface(){};
    }

    public FileData readFileAndCalculateAverages(String path){
        FileData fd = weakHashMap.get(path);
        if(fd != null){
            fd.setFromFile(false);
            return fd;
        }
        List<String> readedFromFile = fileReader.readFile(path);
        if(readedFromFile == null) return null;
        else{
            FileData newFileData = new FileData();
            Integer listSize = readedFromFile.size();
            StringBuilder sb = new StringBuilder();
            Integer counter = 0;
            Float pressureSum = 0.00f;
            Float temperatureSum = 0.00f;
            Integer humiditySum = 0;
            if(listSize == 1){
                newFileData.setPreview(readedFromFile.get(0));
            }else if(listSize > 1){
                if(listSize < 12) {
                    for (String i : readedFromFile) {
                        sb.append(i + "\n");
                    }
                }else{
                    for (int i = 0; i < 12; i++) {
                        sb.append(readedFromFile.get(i) + "\n");
                    }
                }
                newFileData.setPreview((sb.toString()));
                for(Integer i = 1; i < listSize; i++){
                    String pattern = "^\\d{2}:\\d{2}; *(\\d+(\\.\\d+)?); *(-?\\d+(\\.\\d+)?); *(-?\\d+);";
                    Pattern p = Pattern.compile(pattern);
                    Matcher m = p.matcher(readedFromFile.get(i));
                    if (m.find()) {
                        counter ++;
                        pressureSum += Float.parseFloat(m.group(1).replace(",", "."));
                        temperatureSum += Float.parseFloat(m.group(3).replace(",", "."));
                        humiditySum += Integer.parseInt(m.group(5).replace(",", "."));
                    }
                }
                if(counter > 0) {
                    Float averagePressure = (pressureSum / (1.00f * counter));
                    newFileData.setAveragePressure(averagePressure.toString());
                    Float averageTemperature = (temperatureSum / (1.00f * counter));
                    newFileData.setAverageTemperature(averageTemperature.toString());
                    Float averageHumidity = (humiditySum / (1.00f * counter));
                    newFileData.setAverageHumidity(averageHumidity.toString());
                }
            }
            newFileData.setFromFile(true);
            weakHashMap.put(path, newFileData);
            return newFileData;
        }
    }
}

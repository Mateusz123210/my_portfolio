package pl.edu.pwr.weakreferenceslibrary;

public class FileData{

    private String preview;
    private String averagePressure;

    private String averageTemperature;

    private String averageHumidity;

    private Boolean fromFile;

    public FileData(){
        this.preview = "";
        this.averagePressure = "";
        this.averageTemperature = "";
        this.averageHumidity = "";
        this.fromFile = true;
    }

    public String getPreview() {
        return preview;
    }

    public void setPreview(String preview) {
        this.preview = preview;
    }

    public String getAveragePressure() {
        return averagePressure;
    }

    public void setAveragePressure(String averagePressure) {
        this.averagePressure = averagePressure;
    }

    public String getAverageTemperature() {
        return averageTemperature;
    }

    public void setAverageTemperature(String averageTemperature) {
        this.averageTemperature = averageTemperature;
    }

    public String getAverageHumidity() {
        return averageHumidity;
    }

    public void setAverageHumidity(String averageHumidity) {
        this.averageHumidity = averageHumidity;
    }

    public Boolean getFromFile() {
        return fromFile;
    }

    public void setFromFile(Boolean fromFile) {
        this.fromFile = fromFile;
    }

}

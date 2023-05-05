package pl.edu.pwr.impl01;

import ex.api.AnalysisException;
import ex.api.AnalysisService;
import ex.api.DataSet;

public class Impl01 implements AnalysisService, Runnable{
    private DataSet result = null;
    private DataSet ds;
    private boolean errors = false;
    private boolean busy = false;

    @Override
    public void setOptions(String[] options) throws AnalysisException {

    }

    @Override
    public String getName() {
        return "Accuracy";
    }

    @Override
    public void submit(DataSet ds) throws AnalysisException{
        if(busy) throw new AnalysisException("Service is busy");
        busy = true;
        this.ds = ds;
        Thread t1 = new Thread(this);
        t1.start();
    }

    @Override
    public DataSet retrieve(boolean clear) throws AnalysisException {
        if(errors) throw new AnalysisException("Error during processing occured!");
        if(clear){
            DataSet ds1 = result;
            result = null;
            return ds1;
        }
        return result;
    }

    public void calculate() throws AnalysisException{
        result = null;
        errors = false;
        Integer allSum = 0;
        Integer truePredicted = 0;
        String [][] data = ds.getData();
        Integer tempNumber;
        for(int i = 0; i < data.length; i++){
            for(int j = 0; j < data.length; j++){
                try {
                    tempNumber =  Integer.parseInt(data[i][j]);
                    allSum += tempNumber;
                    if(i == j) truePredicted += tempNumber;
                }catch(NumberFormatException e){
                    errors = true;
                    throw new AnalysisException("Data contains characters, which are not numbers!");
                }
            }
        }
        Double accuracy = truePredicted / (1.0 * allSum);
        DataSet res = new DataSet();
        res.setData(new String[][]{{"Accuracy = " + accuracy.toString()}});
        result = res;
        busy = false;
    }

    @Override
    public void run() {
        try {
            calculate();
        } catch (AnalysisException e) {
        }
    }
}
package pl.edu.pwr.discreteconvolutionfunction;

public class DiscreteConvolutionFunction {

    static{
        System.loadLibrary("DiscreteConvolutionFunctionLibrary");
    }

    public native int[][] calculateDiscreteConvolutionFunctionNative(int[][] data, int[][] kernel);

    public int[][] calculateDiscreteConvolutionFunction(int[][] data, int[][] kernel) {
        int dataSize = data.length;
        int kernelSize = kernel.length;
        int [][] kernelFlipped = new int[kernelSize][kernelSize];
        for(int i = 0; i < kernelSize; i++){
            for(int j = 0; j < kernelSize; j++){
                kernelFlipped[kernelSize - 1 - i][kernelSize - 1 - j] = kernel[i][j];
            }
        }
        int resultSize = dataSize - kernelSize + 1;
        int[][] result = new int[resultSize][resultSize];
        int sum;
        for(int i = 0; i < resultSize; i++){
            for(int j = 0; j < resultSize; j++){
                sum = 0;
                for(int k = 0; k < kernelSize; k++){
                    for(int l = 0; l < kernelSize; l++){
                        sum += data[i + k][j + l] * kernelFlipped[k][l];
                    }
                }
                result[i][j] = sum;
            }
        }
        return result;
    }
}

import ex.api.AnalysisService;
import pl.edu.pwr.impl03.Impl03;

module ImplementedService3 {
    requires Api;
    exports pl.edu.pwr.impl03;
    provides AnalysisService with Impl03;


}
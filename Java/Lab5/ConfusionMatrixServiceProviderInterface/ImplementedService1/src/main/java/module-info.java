import ex.api.AnalysisService;
import pl.edu.pwr.impl01.Impl01;

module ImplementedService1 {
    requires Api;
    exports pl.edu.pwr.impl01;
    provides AnalysisService with Impl01;

}
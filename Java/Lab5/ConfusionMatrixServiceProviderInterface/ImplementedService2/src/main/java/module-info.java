import ex.api.AnalysisService;
import pl.edu.pwr.impl02.Impl02;
module ImplementedService2 {
    requires Api;
    exports pl.edu.pwr.impl02;
    provides AnalysisService with Impl02;


}
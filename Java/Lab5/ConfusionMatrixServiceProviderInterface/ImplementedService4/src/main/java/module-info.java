import ex.api.AnalysisService;
import pl.edu.pwr.impl04.Impl04;

module ImplementedService4 {
    requires Api;
    exports pl.edu.pwr.impl04;
    provides AnalysisService with Impl04;
}
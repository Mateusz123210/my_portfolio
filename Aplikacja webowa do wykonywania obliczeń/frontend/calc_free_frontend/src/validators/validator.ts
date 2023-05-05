class Validator {
  emptyMessage = "Nie wpisano równania";
  notMinLengthMessage = "Równanie nie zawiera wszystkich wymaganych znaków";
  linearEquationStartsFromZeroMessage =
    "Równanie mające parametr 0 przy x nie jest liniowe";
  quadraticEquationStartsFromZeroMessage =
    "Równanie mające parametr 0 przy x^2 nie jest kwadratowe";
  invalidEquationMessage = "Wpisane równanie ma niepoprawny format";
  emptyX = "Wpisz wartość współrzędnej x";
  emptyY = "Wpisz wartość współrzędnej y";
  notNumberMessage = "Wpisana wartość nie jest liczbą";
  notNonNegativeNumberMessage =
    "Wpisana wartość nie jest poprawną liczbą nieujemną";
  notNumbersMessage = "Nie wpisano żadnej liczby";
  notWageMessage = "Nie wpisano wagi liczby";
  notValidListOfNumbersMessage = "Wpisz poprawnie listę liczb";
  notEnoughNumbersMessage = "Wpisz długości minimum dwóch boków";
  notValidPositiveNumberMessage = "Wpisz poprawną liczbę dodatnią";
  emptyListMessage = "Lista twoich liczb z wagami jest pusta";
  notValidWeightedAverageListMessage = "Wpisz poprawną listę liczb z wagami";

  checkIfIsNotEmpty = (text: string) => {
    if (text.length > 0) {
      return true;
    }
    return false;
  };

  checkMinimumLength = (text: string, min_length: number) => {
    if (text.length >= min_length) {
      return true;
    }
    return false;
  };

  checkIfIsValidLinearEquation = (text: string) => {
    return /^(-?(\d+(,\d+)?)?)?x([+-]\d+(,\d+)?)?$/.test(
      text.split(" ").join("")
    );
  };
  checkIfIsValidSquareEquation = (text: string) => {
    return /^(-?(\d+(,\d+)?)?)?x\^2(([+-](\d+(,\d+)?)?)?x)?([+-]\d+(,\d+)?)?$/.test(
      text.split(" ").join("")
    );
  };
  checkNotContainsZeroOnStart = (text: string) => {
    return !/^-?0(,0+)?x/.test(text.split(" ").join(""));
  };
  checkIfIsValidNumber = (text: string) => {
    return /^-?\d+(,\d+)?$/.test(text.trimStart());
  };
  checkIfIsValidNonNegativeNumber = (text: string) => {
    if (text.length > 1) {
      return (
        /^\d+(,\d+)?$/.test(text.trimStart()) &&
        !(text.charAt(0) === "0" && text.charAt(1) === "0")
      );
    } else {
      return /^\d+(,\d+)?$/.test(text.trimStart());
    }
  };

  checkIfISValidPositiveNumber = (text: string) => {
    return /^\d+(,\d+)?$/.test(text.trimStart()) && text.charAt(0) !== "0";
  };

  checkIfIsValidListOfNumbers = (text: string) => {
    return /^(-?\d+(,\d+)?;)*(-?\d+(,\d+)?)$/.test(text.split(" ").join(""));
  };

  checkIfIsValidWeightedAverageNumbersWagesList = (text: string) => {
    return /^(-?\d+(,\d+)?\(\d+(,\d+)?\);)*(-?\d+(,\d+)?\(\d+(,\d+)?\))$/.test(
      text.split(" ").join("")
    );
  };

  getWeightedAverageMatches = (text: string) => {
    let temp = text.split(" ").join("");
    return temp.split(";");
  };
}

export default new Validator();

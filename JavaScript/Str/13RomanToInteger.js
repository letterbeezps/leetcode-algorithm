const romanToInt = (
  s,
  romanMap = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000
  }
) =>
  Array.from(s).reduce(
    (acc, cur, idx, src) =>
      romanMap[cur] < romanMap[src[idx + 1]]
        ? (acc -= romanMap[cur])
        : (acc += romanMap[cur]),
    0
  );

var nearestValidPoint = function (x, y, points) {
  let distance = null;
  let tempDistance = null;
  let firstLowest = null;
  let validPoints = false;

  for (var i = 0; i < points.length; i++) {
    let finder = points[i];
    if (x === finder[0] && y === finder[1]) {
      return i;
    }
    if (x == finder[0] || y == finder[1]) {
      validPoints = true;
      tempDistance = Math.abs(x - finder[0]) + Math.abs(y - finder[1]);
      if (distance == null) {
        distance = Math.abs(x - finder[0]) + Math.abs(y - finder[1]);
        // console.log(distance);
      }
      console.log("distance " + distance);
      console.log("tempdistance " + tempDistance);
      console.log(finder);
      if (distance >= tempDistance && tempDistance != null) {
        console.log("distance > temp");

          distance = tempDistance;
          firstLowest = i;

      }
    }
      console.log("First Lowest " + firstLowest);

  }
  if (!validPoints) return -1;
  return firstLowest;
};

let points = [
  [5, 4],
  [3, 4],
  [1, 3],
  [3, 2],
  [1, 7],
  [4, 2],
];
nearestValidPoint(2, 2, points);

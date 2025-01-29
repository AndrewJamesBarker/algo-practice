/**
 * @param {number[][]} intervals
 */
var MergeIntervals = function(intervals) {
  intervals.sort((a,b) => a[0] - b[0]);
  const merged = [];
  for (const interval of intervals) {
    if (merged.length === 0 || merged[merged.length -1][1] < interval[0]) {
      merged.push(interval);
    } else {
      merged[merged.length - 1][1] = Math.max(merged[merged.length - 1][1], interval[1]);
    }
  }
  return merged;
}

const intervals = [[1,3],[2,6],[8,10],[15,18]];
const mergeIntervals = new MergeIntervals(intervals);
console.log(mergeIntervals); // [[1,6],[8,10],[15,18]]
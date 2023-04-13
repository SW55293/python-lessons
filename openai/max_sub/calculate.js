function maxSubArray() {
    // Get the input value
    const input = document.getElementById("input").value;
  
    // Parse the input as a list of integers
    const nums = input.split(",").map((x) => parseInt(x.trim()));
  
    // Call the maxSubArray function and display the result
    const result = document.getElementById("output");
    result.innerText = "Max subarray sum: " + calculateMaxSubArray(nums);
  }
  
  function calculateMaxSubArray(nums) {
    let res = nums[0];
    let total = 0;
    for (let n of nums) {
      total += n;
      res = Math.max(res, total);
      if (total < 0) {
        total = 0;
      }
    }
    return res;
  }
  
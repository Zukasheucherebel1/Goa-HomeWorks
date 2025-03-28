function mostFrequentDigitSum(n) {
    let result = n;
    const digitsSumArr = [];
    
    while(result !== 0) {
      let digitsSum = 0;
      const strN = String(result);
      
      for(let i = 0; i < strN.length; i++) {
        digitsSum += parseInt(strN[i]);
      }
      
      result -= digitsSum;
      digitsSumArr.push(digitsSum);
    }
    
    
    if (digitsSumArr.length === 0) {
      return 0;
    }
    
    
    const frequencyMap = {};
    for (const sum of digitsSumArr) {
      frequencyMap[sum] = (frequencyMap[sum] || 0) + 1;
    }
    
    
    let maxFrequency = 0;
    let mostFrequentSum = -1;
    
    for (const sum in frequencyMap) {
      const frequency = frequencyMap[sum];
      const numSum = parseInt(sum);
      
      if (frequency > maxFrequency || 
          (frequency === maxFrequency && numSum > mostFrequentSum)) {
        maxFrequency = frequency;
        mostFrequentSum = numSum;
      }
    }
    
    return mostFrequentSum;
  }
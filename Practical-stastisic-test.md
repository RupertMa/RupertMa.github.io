---
layout: post
---

# Practical stastisic test | 实用统计检验


#### 1.	Calculate the necessary sample size for A/B test:

[This script](./lib/necessary_sample_size.py) helps you calcualte the minimum group size for your A/B test given the standard error of the metric, the practical significance level.  

The original R script for the calculation is [here](http://video.udacity-data.com.s3.amazonaws.com/topher/2016/December/5845e980_empirical-sizing/empirical-sizing.r). I translated it into Python and improved the efficiency of codes by adding binary search.  

1. Run the following command to see results
```bash
python ./lib/necessary_sample_size.py 0.29 0.02
```


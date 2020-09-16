# 8. Confidence Intervals for One Population Mean

providing information about the accuracy of the estimate is important, which leads to a discussion of confidence intervals, the main topic of this chapter.

- In Section 8.1, we provide the intuitive foundation for confidence intervals.
- In Section 8.2, we present confidence intervals for one population mean when the population standard deviation, $$\sigma$$, is known. Although, in practice, $$\sigma$$ is usually unknown, we first consider, for pedagogical reasons, the case where $$\sigma$$ is known.
- In Section 8.3, we discuss confidence intervals for one population when the population standard deviation is unknown. 

## 8.1 Estimating a Population Mean

- Biased estimation : 표본의 평균이 모집단의 평균과 같음
- Unbiased estimation : 표본의 평군이 모집단의 평균과 다름

### Confidence-Interval Estimation

A sample mean is usually not equal to the population mean; generally, there is sampling error. Therefore, we should accompany any point estimate of $$\mu$$ with information that indicates the accuracy of that estimate. 

- This information is called a confidence-interval estimate for $$\mu$$ 
- A confidence interval for a population mean depends on the sample mean

### Interpreting Confidence Intervals

- Standard Deviation of the Sample Mean : $$\sigma_x = \frac{\sigma}{\sqrt{n}}$$
- Margin of Error : Standard Deviation of the Sample Mean * 2 
- Confidence intervals : Margin of Error * 2

## 8.3 Confidence Intervals for One Population Mean When $$\sigma$$ is Unknown

What if, as is usual in practice, the population standard deviation is unknown?

1. When we know standard deviation(Standardized version of $$\bar{x}$$)

$$
z = \frac{\bar{x} - \mu}{\sigma / \sqrt{n}}
$$

2. When we don't know standard deviation (Studentized version of $$\bar{x}$$ )

$$
t = \frac{\bar{x} - \mu}{s / \sqrt{n}}
$$

- `s` : Sample standard deviation
- Studentized : 표준화된
- ***The studentized version has more spread than the standardized version***.
  - This difference is not surprising because the variation in the possible values of the standardized version is due solely to the variation of sample means, whereas that of the studentized version is due to the variation of both sample means and sample standard deviations
  - 표준화된 경우 더 넓은 분포를 갖는데, 표준화 전에는 모집단의 표준 편차를 사용해서 고정 된 값이지만, 표준화 했을 때 표준편차는 표본의 표준 편차를 사용하기 때문에 더 다양한 값을  갖음.
  - 표준화 된 분포를 t-distribution 또는 Student's t-distribution이라 불림

### t-Distributions and t-Curves

There is a different t-distribution for each sample size.

- We identify a particular t-distribution by its ***number of degrees of freedom (df)***.
- For the studentized version of $$\bar{x}$$, the number of degrees of freedom is 1 less than the sample size, which we indicate symbolically by $$df = n − 1$$.
- A variable with a t-distribution has an associated curve, called a t-curve.

#### Basic Properties of t-Curves

- Property 1: The total area under a t-curve equals 1.
- Property 2: A t-curve extends indefinitely in both directions, approaching, but never touching, the horizontal axis as it does so.
- Property 3: A t-curve is symmetric about 0.
- Property 4: As the number of degrees of freedom becomes larger, t-curves look increasingly like the standard normal curve.

For a t-curve with $$\nu$$ (pronounced “new”) degrees of freedom, where $$\nu$$ > 2, the standard deviation $$\sqrt{\nu/(\nu - 2)}$$. This quantity always exceeds 1, which is the ***standard deviation of the standard normal curve***.
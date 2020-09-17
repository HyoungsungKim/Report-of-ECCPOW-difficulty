# Hypothesis Tests for One Population Mean

To make that decision, we can take a random sample of people imprisoned last year for drug offenses, compute their sample mean sentence, $$\bar{x}$$, and then apply a statistical-inference technique called a ***hypothesis test***.

In this chapter, we describe hypothesis tests for one population mean. In doing so, we consider three different procedures.

- The first two are called the one-mean z-test and the one-mean t-test, which are the hypothesis-test analogues of the one-mean z-interval and one-mean t-interval confidence-interval procedures, respectively, discussed in Chapter 8.
- The third is a nonparametric method called the ***Wilcoxon signed-rank test***, which applies when the variable under consideration has a symmetric distribution.

We also examine two different approaches to hypothesis testing—namely, the critical-value approach and the P-value approach.

## 9.1 The Nature of Hypothesis Testing

A hypothesis is a statement that something is true. For example, the statement “the mean weight of all bags of pretzels packaged differs from the advertised weight of 454 g” is a hypothesis. Typically, a hypothesis test involves two hypotheses: the ***null hypothesis*** and the ***alternative hypothesis*** (or research hypothesis)

- Null hypothesis: A hypothesis to be tested. We use the symbol $$H_0$$ to represent the null hypothesis.
- Alternative hypothesis: A hypothesis to be considered as an alternative to the null hypothesis. We use the symbol $$H_a$$ to represent the alternative hypothesis.
- Hypothesis test: The problem in a hypothesis test is to decide whether the null hypothesis should be rejected in favor of the alternative hypothesis.

For instance, in the pretzel packaging example, the null hypothesis might be “the mean weight of all bags of pretzels packaged equals the advertised weight of 454 g,” and the alternative hypothesis might be “the mean weight of all bags of pretzels packaged differs from the advertised weight of 454 g.”

### Choosing the Hypotheses

The first step in setting up a hypothesis test is to decide on the null hypothesis and the alternative hypothesis. The following are some guidelines for choosing these two hypotheses. Although the guidelines refer specifically to hypothesis tests for one population mean, $$\mu$$, they apply to any hypothesis test concerning one parameter.

- Null Hypothesis : $$H_0: \mu = \mu_0$$
- Alternative Hypothesis
  - The choice of the alternative hypothesis depends on and should reflect the purpose of the hypothesis test. Three choices are possible for the alternative hypothesis.
  - If the primary concern is deciding whether a population mean, $$\mu$$, is different from a specified value $$\mu_0$$ , we express the alternative hypothesis as $$H_a: \mu \neq \mu_0$$.
    - A hypothesis test whose alternative hypothesis has this form is called a ***two-tailed test***. 
  - If the primary concern is deciding whether a population mean, $$\mu$$ , is less than a specified value $$μ_0$$, we express the alternative hypothesis as $$H_a: μ < μ_0$$.
    - A hypothesis test whose alternative hypothesis has this form is called a ***left-tailed test***. 
  - If the primary concern is deciding whether a population mean, $$\mu$$ , is greater than a specified value $$\mu_0$$, we express the alternative hypothesis as $$H_a: \mu > \mu_0 $$.
    - A hypothesis test whose alternative hypothesis has this form is called a ***right-tailed test***.
  - A hypothesis test is called a ***one-tailed test*** if it is either left tailed or right tailed.

### The Logic of Hypothesis Testing

***After we have chosen the null and alternative hypotheses, we must decide whether to reject the null hypothesis in favor of the alternative hypothesis***.

> ### Basic Logic of Hypothesis Testing
>
> Take a random sample from the population. If the sample data are consistent with the null hypothesis, do not reject the null hypothesis; if the sample data are inconsistent with the null hypothesis and supportive of the alternative hypothesis, reject the null hypothesis in favor of the alternative hypothesis.
>
> - 샘플 뽑은게 null hypothesis와 비슷하면 alternative hypothesis 버릴 수 있음
> - 반대도 마찬가지

In practice, of course, we must have a precise criterion for deciding whether to reject the null hypothesis. At this point, we simply note that a precise criterion involves a ***test statistic***, a statistic calculated from the data that is used as a basis for deciding whether the null hypothesis should be rejected.

### Type 1 and Type 2 Errors

|                        |       True       |      False       |
| :--------------------: | :--------------: | :--------------: |
| Do not reject $$H_0 $$ | Correct decision |   Type 2 error   |
|    Reject $$H_0 $$     |   Type 1 error   | Correct decision |

- Type I error: Rejecting the null hypothesis when it is in fact true.
  - Null hypothesis가 맞는데 틀리다고 하는 것
- Type II error: Not rejecting the null hypothesis when it is in fact false.
  - Null hypothesis가 틀린데 맞나고 하는 것
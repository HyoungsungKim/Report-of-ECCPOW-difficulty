# Chi-Square Procedures

In this chapter, we consider three widely used inferential procedures that are not concerned with population parameters. These three procedures are often called chi-square procedures because they rely on a distribution called the chi-square distribution

## 13.1 The Chi-Square Distribution

Basic Properties of  $$\chi ^2$$-Curves

- Property 1: The total area under a $$\chi ^2$$-curve equals 1.
- Property 2: A  $$\chi ^2$$-curve starts at 0 on the horizontal axis and extends indefinitely to the right, approaching, but never touching, the horizontal axis.
- Property 3: A  $$\chi ^2$$-curve is right skewed.
- Property 4: As the number of degrees of freedom becomes larger,  $$\chi ^2$$-curves look increasingly like normal curves.

### Using the $$\chi ^2$$ - Table

To perform a chi-square test, we need to know how to find the $$\chi ^2$$ - value that has a specified area to its right.

## 13.2 Chi-Square Goodness-of-Fit Test

Our first chi-square procedure is called the chi-square goodness-of-fit test. We can use this procedure to perform a hypothesis test about the distribution of a qualitative (categorical) variable or a discrete quantitative variable that has only finitely many possible values.

- Chi-Square

$$
\sum(O-E)^2/E
$$

- $$O$$ : Observed frequencies
- E : Expected frequencies
- Can this value be reasonably attributed to sampling error, or is it large enough to suggest that the null hypothesis is false? To answer this question, we need to know the distribution of the test statistic $$\sum(O-E)^2/E$$.

### Procedure for the Chi-Square Goodness-of-Fit Test

Purpose

- To perform a hypothesis test for the distribution of a variable

Assumptions

1. All expected frequencies are 1 or greater
2. At most 20% of the expected frequencies are less than 5
3. Simple random sample

Step 1 The null and alternative hypotheses are, respectively,

- $$H_0$$: The variable has the specified distribution
- $$H_a$$: The variable does not have the specified distribution.

Step 2  Decide on the significance level, α.

Step 3  Compute the value of the test statistic
$$
\chi^2 = \sum(O-E)^2/E
$$
where O and E represent observed and expected frequencies, respectively. Denote the value of the test statistic $$χ_0^2$$.


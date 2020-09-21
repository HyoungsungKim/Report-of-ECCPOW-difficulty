# Research proposal

## Contents

1. 문제
2. 실험 계획 및 예상 결과
   1. 데이터 샘플 증가 시켰을때 outlier 관측
   2. 난이도 조절에 사용되는 `n`을 증가 시켰을 때 outlier 관측
3. 문헌 조사(진행 중)
4. 향후  ECCPoW 개발 계획

## 1. 문제

블록을 1500개 생성 했을 때의 히스토그램(bin=1500)

![histogram](/home/hskim/Documents/github-repos/Report-of-ECCPOW-difficulty /img/histogram.png)

- 데이터 샘플이 부족해 지수분포인지, 혹은 Heavy tail 분포인지 확신 할 수 없음
  - 만약 지수분포가 아니라 Heavy tail이라면 블록 생성 시간 통제가 불가능 함
- 따라서 난이도 조절에 사용되는 parameter인 `n`을 바꿨을 때 지수 분포를 얻을 수 있는지 확인이 필요함
  - 지수분포의 rate($$\lambda$$)를 알고 있다면 확률 분포를 쉽게 얻을 수 있음
    - $$y = e^{-\lambda t}$$
  - 하지만 실험으로 얻은 샘플로 계산한 rate($$\lambda$$)가 실제 rate($$\lambda$$)와 얼마나 일치하는지 확신 알 수 없음
  - 샘플을 얻는데 시간이 매우 오래 걸리기 때문에 rate($$\lambda$$) 추정에 필요한 충분한 샘플을 얻을 수 없음
  - 따라서 샘플로 얻은 rate($$\lambda$$)로 실제 rate($$\lambda$$)를 어떻게 추정 할 것인가 방법 필요
- 어떻게 outlier를 정의 할 것인가? 정의 필요

## 2.  실험 계획 및 예상 결과

1. 데이터 샘플 증가 시켰을때 outlier 관측

- 데이터 샘플 개수에 따라 outlier를 관측 함. 만약 ECCPoW로 생성되는 블록이 지수분포를 갖는다면, 데이터 샘플이 증가 할 수록 outlier가 감소할 것으로 예상 됨

2. 난이도 조절에 사용되는 `n`을 증가 시켰을 때 outlier 관측

- 현재 ECCPoW의 난이도 조절은 `n`의 길이와  decision step사이의 1의 개수에 의해 조절 됨. 이번 실험에서 n의 길이 변화로만 실험 함.
- n의 길이를 증가 시키고 1번의 실험을 반복함. 1번 실험을 반복하여 얻은 결과로 지수 분포 임을 알 수 있다면 n의 길이를 조절 하여 ASIC 저항성을 가지면서 블록 생성 시간을 통제 할 수 있음.

## 3. 문헌 조사

wikipedia

- exponential distribution : https://en.wikipedia.org/wiki/Exponential_distribution
- exponential distribution 2 : http://reliawiki.org/index.php/The_Exponential_Distribution#Estimation_of_the_Exponential_Parameters
- heavy-tail distribution : https://en.wikipedia.org/wiki/Heavy-tailed_distribution
- Outlier : https://en.wikipedia.org/wiki/Outlier
- Anomaly detection : https://en.wikipedia.org/wiki/Anomaly_detection
- Censoring (statistics) : https://en.wikipedia.org/wiki/Censoring_(statistics)
  - In statistics, censoring is a condition in which the value of a measurement or observation is only partially known. 
- Failure rate : https://en.wikipedia.org/wiki/Failure_rate

article

- Real-time anomaly detection with exponentially-distributed data : https://towardsdatascience.com/real-time-anomaly-detection-with-exponentially-distrubted-data-205e0df32096
- ML estimate of exponential distribution (with censored data) : https://stats.stackexchange.com/questions/133347/ml-estimate-of-exponential-distribution-with-censored-data
- Standford lecture material : https://web.stanford.edu/~lutian/coursepdf/unit2.pdf
- Parameter estimation of exponential distribution with biased sampling : https://stats.stackexchange.com/questions/45001/parameter-estimation-of-exponential-distribution-with-biased-sampling

paper

- The identification of outliers in exponential samples : https://onlinelibrary.wiley.com/doi/pdf/10.1111/1467-9574.01600
- Big Outliers Versus Heavy Tails:  what to use? : https://arxiv.org/pdf/1611.05410.pdf
- On the Kolmogorov-Smirnov Test for the Exponential Distribution with Mean Unknown
- (국내)T test as a parametric statistic :  https://ekja.org/upload/pdf/kjae-68-540_ko.pdf

## 4. 향후  ECCPoW 개발 계획

1.  bootnode 지정
2.  Docker file 생성 및 배포

